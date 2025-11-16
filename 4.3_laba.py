from function import file_read
from function import file_write
filename = 'example.txt'
content = file_write(filename, 'как дела?')
print(content)
answer = file_read(filename)
print('Текущий текст в файле:', filename, 'будет:', answer)

from function import is_prime
pas = is_prime(2)
print(pas)
if pas == True:
    print('число простое')
else:
    print('число не простое')

from function import string_lower
des = string_lower('ПРИВЕТ')
print(des)