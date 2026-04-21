import numpy as np

arr = np.array([12, 25, 8, 32, 65, 18, 4])
mask = arr > 20
print(f'Маска: {mask}')
filtered = arr[mask]
print(f'Элементы которые > 20: {filtered}')

# два условия одновременно
mask2 = (arr >10) & (arr < 30)
print(f'Элементы которыые >10 и <30: {arr[mask2]}')

arr_copy = arr.copy()
arr_copy[arr_copy < 20] = 0
print(f'Массив после замены элементов <20 на 0: {arr_copy}')