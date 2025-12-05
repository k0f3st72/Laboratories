def write_to_file(filename, text):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return "Текст добавлен в файл"
    except FileNotFoundError:
        return f'Файл {filename} не найден'

def append_to_file(filename):
    try:
        add_text = input('Введите дополнительный текст: ')
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(' ' + add_text)
        return 'Текст добавлен в файл'
    except FileNotFoundError:
        return f'Файл {filename} не найден'

def file_read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f'Файл {filename} не найден'

filename = '../example.txt'
text = input('Введите текст для записи в файл: ')
def file_operations():
    result = write_to_file(filename, text)
    print(result)

    while True:
        result = file_read(filename)
        print('Текущий текст', result)

        question = input('Добавить ещё текст? (да/нет): ').lower()
        if question == 'нет':
            return 'Работа с файлом завершена'

        result = append_to_file(filename)
        print(result)

result = file_operations()
print(result)