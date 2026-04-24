from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel, ValidationError, field_validator
from datetime import datetime
import json
from typing import Dict, Optional
import uvicorn

app = FastAPI()

html_file = Path(__file__).parent / "chat.html"

active_connections: Dict[str, WebSocket] = {}

# Модель для валидации входящих сообщений
class ChatMessage(BaseModel):
    type: str = "message"
    text: str
    user: Optional[str] = None
    to: Optional[str] = None
    ts: Optional[str] = None

    @field_validator("text")
    @classmethod
    def validate_text(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Message cannot be empty")
        if len(v) > 200:
            raise ValueError("Message is too long (max 200 characters)")
        return v.strip()


def get_timestamp() -> str:
    return datetime.now().isoformat()


async def send_system_message(websocket: WebSocket, message: str, online_count: int):
    system_msg = {
        "type": "system",
        "text": message,
        "online": online_count,
        "ts": get_timestamp()
    }
    await websocket.send_text(json.dumps(system_msg, ensure_ascii=False))


async def broadcast_system_message(message: str, exclude_user: Optional[str] = None):
    online_count = len(active_connections)
    system_msg = {
        "type": "system",
        "text": message,
        "online": online_count,
        "ts": get_timestamp()
    }

    for username, connection in active_connections.items():
        if username != exclude_user:
            try:
                await connection.send_text(json.dumps(system_msg, ensure_ascii=False))
            except:
                pass


async def broadcast_message(message_data: dict, exclude_user: Optional[str] = None):
    online_count = len(active_connections)
    message_data["online"] = online_count

    for username, connection in active_connections.items():
        if username != exclude_user:
            try:
                await connection.send_text(json.dumps(message_data, ensure_ascii=False))
            except:
                pass


async def send_private_message(from_user: str, to_user: str, text: str):
    if to_user not in active_connections:
        # Получатель не найден
        if from_user in active_connections:
            error_msg = {
                "type": "error",
                "detail": f"User '{to_user}' is not online",
                "ts": get_timestamp()
            }
            await active_connections[from_user].send_text(json.dumps(error_msg, ensure_ascii=False))
        return False

    # Отправляем приватное сообщение
    private_msg = {
        "type": "private",
        "from": from_user,
        "to": to_user,
        "text": text,
        "ts": get_timestamp(),
        "online": len(active_connections)
    }

    try:
        await active_connections[to_user].send_text(json.dumps(private_msg, ensure_ascii=False))

        # Отправляем подтверждение отправителю
        confirm_msg = {
            "type": "private_sent",
            "to": to_user,
            "text": text,
            "ts": get_timestamp()
        }
        await active_connections[from_user].send_text(json.dumps(confirm_msg, ensure_ascii=False))

        return True
    except:
        return False


@app.get("/")
async def get():
    html = html_file.read_text(encoding='utf-8')
    return HTMLResponse(content=html, status_code=200)


@app.websocket("/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        username: str = Query(..., min_length=1, max_length=50)
):

    # Проверка на уникальность имени
    if username in active_connections:
        await websocket.close(code=1008, reason="Username already taken")
        return

    await websocket.accept()

    # Сохраняем соединение
    active_connections[username] = websocket

    # Отправляем приветствие при заходе
    await send_system_message(
        websocket,
        f"Welcome {username}! You are now connected.",
        len(active_connections)
    )

    # Рассылаем всем остальным о подключении нового пользователя
    await broadcast_system_message(f"{username} joined", exclude_user=username)

    try:
        while True:
            # Получаем сообщение от клиента
            data = await websocket.receive_text()

            try:
                # Парсим JSON
                raw_message = json.loads(data)

                # Проверяем, не является ли сообщение командой приватного сообщения
                if raw_message.get("type") == "command":
                    command_text = raw_message.get("text", "")
                    if command_text.startswith("/w "):
                        # Парсим команду /w username message
                        parts = command_text[3:].split(" ", 1)
                        if len(parts) == 2:
                            target_user, private_text = parts
                            await send_private_message(username, target_user, private_text)
                        else:
                            # Неверный формат команды
                            error_msg = {
                                "type": "error",
                                "detail": "Invalid command format. Use: /w username message",
                                "ts": get_timestamp()
                            }
                            await websocket.send_text(json.dumps(error_msg, ensure_ascii=False))
                    else:
                        error_msg = {
                            "type": "error",
                            "detail": f"Unknown command: {command_text}",
                            "ts": get_timestamp()
                        }
                        await websocket.send_text(json.dumps(error_msg, ensure_ascii=False))
                    continue

                # Валидируем
                validated_msg = ChatMessage(**raw_message)

                # Добавляем имя пользователя и время
                message_to_send = {
                    "type": "message",
                    "user": username,
                    "text": validated_msg.text,
                    "ts": get_timestamp()
                }

                # Рассылаем всем
                await broadcast_message(message_to_send, exclude_user=None)

            except json.JSONDecodeError:
                # Некорректный JSON
                error_msg = {
                    "type": "error",
                    "detail": "Invalid JSON format",
                    "ts": get_timestamp()
                }
                await websocket.send_text(json.dumps(error_msg, ensure_ascii=False))

            except ValidationError as e:
                # Ошибка валидации
                error_msg = {
                    "type": "error",
                    "detail": str(e.errors()[0].get("msg", "Validation error")),
                    "ts": get_timestamp()
                }
                await websocket.send_text(json.dumps(error_msg, ensure_ascii=False))

    except WebSocketDisconnect:
        # Удаляем пользователя при отключении
        if username in active_connections:
            del active_connections[username]

        # Рассылаем всем о выходе пользователя
        await broadcast_system_message(f"{username} left")

    except Exception as e:
        # Обработка других ошибок
        print(f"Error: {e}")
        if username in active_connections:
            del active_connections[username]
        await broadcast_system_message(f"{username} left")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)