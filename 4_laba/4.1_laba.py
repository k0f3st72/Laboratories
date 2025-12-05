import math

try:
    number = int(input("Введите число: "))
    result = math.sqrt(number)
    print(f'Квадратный корень из {number} равен {result}')
except ValueError as a:
    print(f'Ошибка: {a}')

#zadanie 1.2
from datetime import date, datetime

clock = datetime.now()
today = date.today()

print(f' время: {clock.time()}, дата: {today}')