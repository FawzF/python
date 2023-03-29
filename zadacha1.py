number = int(input("Введите число: "))
borderline = int(input("Введите пограничное число: "))

if number < borderline:
    print("Число меньше пограничного")
elif number > borderline and number <= borderline*3:
    print("Число больше пограничного")
else:
    print("Число больше пограничного более, чем в 3 раза")