name = str(input('Введите ваше имя: '))
age = int(input('Введите ваш возраст (Если не хотите указывать возраст, напишите 0): '))

def describe_person(name, age):
    if age == 0:
        return print('Вас зовут', name, 'вам', age+30)
    elif age > 0:
        return print('Вас зовут', name, 'вам', age)
    else:
        return print('Вы неправильно ввели свой возраст')

describe_person(name, age)
