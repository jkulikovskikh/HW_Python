# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число: "))
print(n // 100 + (n // 10) % 10 + n % 10)