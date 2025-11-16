#zadanie 1.1
try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Файл не существует')

#zadanie 1.2
try:
    with open('exmple.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print('Файл не существует')