# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Введите сумму натуральных чисел: "))
pow = int(input("Введите произведение натуральных чисел: "))

if sum > 2000:
    print("По условию загаданные числа меньше либо равны 1000")
elif sum <= 1:
    print("По условию загаданные числа - натуральные числа и их сумма должна быть больше 1")
elif pow <= 0:
    print("По условию загаданные числа - натуральные числа и их произведение должно быть больше 0")
else:
    D = sum ** 2 - 4 * pow
    if D < 0:
        print("Загаданные числа не натуральные")
    else:
        y = (sum + D ** 0.5) / 2
        x = sum - y
        print(int(x), int(y))
