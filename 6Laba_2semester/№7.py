import time
import numpy as np

arr_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arr_int64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
arr_float32 = np.array([1, 2, 3, 4, 5], dtype=np.float32)
arr_float64 = np.array([1, 2, 3, 4, 5], dtype=np.float64)

print("int32 массив:", arr_int32, "| память:", arr_int32.nbytes, "байт")
print("int64 массив:", arr_int64, "| память:", arr_int64.nbytes, "байт")
print("float32 массив:", arr_float32, "| память:", arr_float32.nbytes, "байт")
print("float64 массив:", arr_float64, "| память:", arr_float64.nbytes, "байт")

arr_float_from_int = arr_int32.astype(np.float64)
print(f"Преобразование из int32 в float64: {arr_float_from_int}")
arr_small_int = np.array([1, 2, 3], dtype=np.int32)
print(f"int32: {arr_small_int}/2 = {arr_small_int/2}")
arr_small_float = np.array([1, 2, 3], dtype=np.float64)
print(f"float64: {arr_small_float}/2 = {arr_small_float/2}")

size = 10_000_000
np_array = np.arange(size, dtype=np.float64)
start = time.time()
sum_np = np.sum(np_array)
end = time.time()
print(f"Сумма: {sum_np}")
print(f"Время начала: {start}")
print(f"Время завершения: {end}")
print(f"Всё длилось: {end - start}")

