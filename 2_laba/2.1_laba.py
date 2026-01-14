#Задание 1
name = str(input('Введите Имя:'))
def greet(name):
    print('привет', name)
greet(name)

#Задание 1(2)
number = int(input('Введите число: '))
def square(number):
    n = number**2
    print('Число в квадрате: ', n)
square(number)

#zadanie 1(3)
x = int(input('Первое число:'))
y = int(input('Второе число:'))

def max_of_two(x, y):
    if x > y:
        return print(x)
    elif x < y:
        return print(y)
    else:
        return print(x)
max_of_two(x, y)
