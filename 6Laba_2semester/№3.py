import numpy as np
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print(f"Форма: {matrix.shape}")
print(f"  По всем элементам: {np.sum(matrix)}")
#Сумма
print(f"  По строкам : {np.sum(matrix, axis=1)}")
print(f"  По столбцам : {np.sum(matrix, axis=0)}")
#Среднее
print(f"  По строкам (axis=1): {np.mean(matrix, axis=1)}")
print(f"  По столбцам (axis=0): {np.mean(matrix, axis=0)}")
#Минимум
print(f"  По строкам (axis=1): {np.min(matrix, axis=1)}")
print(f"  По столбцам (axis=0): {np.min(matrix, axis=0)}")
#Максимум
print(f"  По строкам (axis=1): {np.max(matrix, axis=1)}")
print(f"  По столбцам (axis=0): {np.max(matrix, axis=0)}")
