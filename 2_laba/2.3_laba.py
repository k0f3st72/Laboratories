def is_prime(number):
    if number < 2:
        print(f'{number} - сложное число')
        return False
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - сложное число')
            return False
    print(f"{number} - простое число")
    return True


while True:
    number = input('Введите ваше число для проверки простого числа(Или стоп для остановки):')
    if number.lower() == 'стоп':
            print('Пока-пока <3')
            break
    try:
        num = int(number)
        is_prime(num)
        print('Ваше число целое!')
    except ValueError:
        print('Ваше число не целое :(')
        continue