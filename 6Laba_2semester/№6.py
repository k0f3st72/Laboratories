import numpy as np

#Одномерный массив
arr = np.array([38, 26, 65, 14, 29, 93, 48, 72, 26, 35, 9, 12, 3])

sorted_arr = np.sort(arr)
print(f'Отсартированный массив: {sorted_arr}')

sort_asc = np.sort(arr)
sort_desc = np.sort(arr)[::-1]
print(f"По убыванию: {sort_desc}")
print(f"По возрастанию: {sort_asc}")

indices = np.argsort(arr)
print(f"Индексы для сортировки: {indices}")
print(f"Элементы по индексам: {arr[indices]}")

index_max = np.argmax(arr)
print(f"Индекс маскимального элемента: {index_max}")
print(f"Максимальный элемент: {arr[index_max]}")

index_min = np.argmin(arr)
print(f"Индекс минимального элемента: {index_min}")
print(f"Минимальный элемент: {arr[index_min]}")

# Двумерный массив
matrix = np.array([[4, 7, 2 ],
                   [1, 8, 6],
                   [3, 9, 1]])

print(f"Сортировка по строкамиx: {np.sort(matrix, axis=1)}")
print(f"Сортировка по столбцам: {np.sort(matrix, axis=0)}")
print(f"Индекс максимума по все матрице: {np.argmax(matrix)}")
print(f"Максимуму по строкам: {np.argmax(matrix, axis=1)}")
print(f"Максимум по столбцам: {np.argmax(matrix, axis=0)}")









