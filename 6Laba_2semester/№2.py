import numpy as np
a = np.array([[10, 20, 30]])
b = np.array([[40, 50, 60]])
print(a+b)
print(a*b)
print(a+10)
print(b*2)
print("Сумма :", np.sum(a))
print("Среднее значение: ", np.mean(a))
print("Минимальный элемент :", np.min(a))
print("Максимальный элемент :", np.max(a))
print("Отклонение: ", np.std(a))

# ============Python==================
py_list = [15, 23, 32, 52, 46, 75]
py_list2 = [1, 2, 3, 4, 5, 6,7]

print("Сумма: ", sum(py_list))
print(f"Среднее: ", sum(py_list)/len(py_list))
print(f"Минимум: ", min(py_list))
print(f"Максимум: ", max(py_list))
