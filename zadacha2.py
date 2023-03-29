string = input("Введите строку: ")
c = 0
for index, char in enumerate(string):
    if (index + 1) == 3:
        continue
    if char == "c":
        c = 1
    if index != len(string) - 1:
        print(char, end="")
if c == 1:
    print("\nСимвол 'c' обнаружен")
print("\nДлина строки:", len(string))