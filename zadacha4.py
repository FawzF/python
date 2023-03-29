import math
import random

# Список доступных операций
print("Доступные операции:")
print("+ - сложение")
print("- - вычитание")
print("/ - деление")
print("* - умножение")
print("** - возведение в степень")
print("abs - модуль числа")
print("random - рандомное число от 0 до введенного")
print("! - факториал числа")
print("acos - арккосинус (в радианах)")

# Считываем операцию
operation = input("Введите операцию: ")

# Ввод чисел
if operation in ["+", "-"]:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
elif operation == "/":
    num1 = float(input("Введите делимое: "))
    num2 = float(input("Введите делитель: "))
    if num2 == 0:
        print("Деление на ноль невозможно.")
        exit()
elif operation == "*":
    num1 = float(input("Введите первый множитель: "))
    num2 = float(input("Введите второй множитель: "))
elif operation == "**":
    num1 = float(input("Введите число, которое нужно возвести в степень: "))
    num2 = float(input("Введите показатель степени: "))
elif operation == "abs":
    num1 = float(input("Введите число: "))
elif operation == "random":
    num1 = float(input("Введите верхнюю границу для рандомного числа: "))
elif operation == "!":
    num1 = int(input("Введите число, для которого нужно найти факториал: "))
    if num1 < 0:
        print("Факториал отрицательного числа не существует.")
        exit()
elif operation == "acos":
    num1 = float(input("Введите число для вычисления арккосинуса (в радианах): "))
    if num1 < -1 or num1 > 1:
        print("Аргумент арккосинуса должен находиться в диапазоне [-1, 1].")
        exit()

# Вывод результата
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "**":
    print(num1 ** num2)
elif operation == "abs":
    print(abs(num1))
elif operation == "random":
    print(random.randint(0, int(num1)))
elif operation == "!":
    print(math.factorial(num1))
elif operation == "acos":
    print(math.acos(num1))