import numpy as np

#Одномернный массив
arr1d = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("Форма: ", arr1d.shape)
print("Тип данных: ",arr1d.dtype)
print("Размерность: ",arr1d.ndim)
print("Количество элементов: ",arr1d.size)

#Доступ к элементам 1D
print("Элемент с индексом 2: ", arr1d[2])
print(" Срез [4:9]: ", arr1d[4:9])
print("Срез с шагом 2: ", arr1d[::2])

print("="*30)
#Двумернный массив
arr2d = np.array([[10,20,30],
                  [40,50,60],
                  [70,80,90]])
print("Форма: ", arr2d.shape)
print("Тип данных: ",arr2d.dtype)
print("Размерность: ",arr2d.ndim)
print("Количество элементов: ",arr2d.size)

#Доступ к элементам 2D
print("Элемент [1:2]: ", arr2d[1:2])
print("Строка 1, без столбцов: ", arr2d[0, :])
print("Без строк, с 1 столбцом", arr2d[:, 0])
print("2x2: ", arr2d[:2, :2])