from fileinput import filename


def file_read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f'Файл {filename} не найден'

def file_write(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return f'Содержимое записано в {filename}'

def append_to_file():
    add_text = input('Введите дополнительный текст: ')
    with open('user_input.txt', 'a', encoding='utf-8') as file:
        file.write(' ' + add_text)
    return f'Текст добавлен в файл {filename()}'