"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number1 = int(input("Введите число n: "))
calculation1 = str(number1) + str(number1 + number1) + str(number1 + number1 + number1)
print(str(number1) +" + "+ str(number1) + str(number1) +" + "+ str(number1) + str(number1) + str(number1) +" = " + calculation1)

