class UserAccount:
    def __init__(self, username, email ,password):
        self.username = username
        self.email = email
        self.__password = password

    def strong_password(self, password):
        if len(password) < 6:
            raise ValueError("Пароль должен содержать минимум 6 символов")
        return password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, replay_password):
        return self.__password == replay_password

    def get_password_mask(self):
        return "*" * len(self.__password)

    def get_password_for_debug(self):
        return self.__password

username = input('Введите ник: ')
email = input('Введите почту: ')

while True:
    password = input('Введите пароль : ')
    if len(password) >= 6:
        break
    else:
        print('✗ Пароль должен состоять минимум из 6 символов!')
        print('Попробуйте еще раз')

user = UserAccount(username, email, password)

while True:
    password_to_check = input('Введите старый пароль ещё раз: ')
    if user.check_password(password_to_check):
        print('Пароль верный')
        break
    else:
        print("Пароль неверный, попробуйте ещё раз")

new_password = input("Введите новый пароль: ")
user.set_password(new_password)

while True:
    newpassword_to_check = input('Введите пароль ещё раз: ')
    if len(newpassword_to_check) >= 6:
        break
    else:
        print('Пароль должен быть больше 6 символов')
        print('Попробуйте ещё раз')

if user.check_password(newpassword_to_check):
    print('Пароль верный')
else:
    print('Пароль неверный')

print(f'Ник: {user.username}')
print(f'Почта: {user.email}')
print(f'Скрытый Пароль: {user.get_password_mask()}')

while True:
    try:
        visible_password = input('Если вы хотите увидеть ващ пароль напишите (да/нет): ')
        if visible_password != 'да':
            break
        else:
            print(f'Видимый пароль: {user.get_password_for_debug()}')
            break
    except (EOFError):
        print("Ошибка: вы ввели аббракадабру")