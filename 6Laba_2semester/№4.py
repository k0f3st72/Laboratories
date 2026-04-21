import numpy as np

#Арифметика
col_vec = np.array([[1], [2], [3]])
row_vec = np.array([10, 20, 30])

print(col_vec)
print(row_vec)
print("Форма: ", col_vec.shape, "Форма: ", row_vec.shape)
print(col_vec+row_vec) #3x3
print(col_vec*row_vec) #3x3
result = col_vec + row_vec
print("Форма: ", result.shape)

#массив + скаляр
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],])
x = 10
result2 = matrix + x
print("Матрица + скаляр: ")
print(result2)
print("Матрица + скаляр: ")
print(result2.shape)

#массив + вектор-строка
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],])
vector = np.array([10, 20, 30, 40])
result3 = matrix + vector
print("Сумма: ", result3)
print("Сумма: ", result3.shape)


