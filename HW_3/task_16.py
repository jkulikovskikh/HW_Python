# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

N = int(input("Введите количество элементов в массиве: "))

A = [random.randint(1, N) for i in range(N)]
print(A)

X = int(input("Введите число: "))
print(f"Число {X} втречается в массиве {A.count(X)} раз")