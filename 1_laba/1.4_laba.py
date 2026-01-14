n = int(input("\nВведите число для вывода от 1 до него: "))
for i in range(1, n + 1):
    print(i)

# Задача 2
a = int(input("\nВведите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Большее число:", a)
else:
    print("Большее число:", b)