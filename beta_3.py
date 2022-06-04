# Дан словарь:
# days = { 1:'Sun', 2:'Mon', 3:'Tue',
# 4:'Wed', 5:'Thu', 6:'Fri', 7:’Sat’}
# Записать его в файл
# построчно.

days = {1: "Sun", 2: "Mon", 3: "Tue", 4: "Wed", 5: "Thu", 6: "Fri", 7: "Sat"}
with open("days.txt", "w") as f:
    for k, v in days.items():
        f.write(str(k) + ":" + str(v) + "\n")
print(type(days))

# Прочитать предыдущий файл,
# сформировать из него словарь,
# распечатать его

days_2 = {}
with open("days.txt", "r") as f:
    for lines in f:
        string = lines.split(":")
        key = int(string[0])
        value = string[1].rstrip()
        days_2[key] = value
print(days_2)
print(type(days_2))

# Создать множество
# отрицательных и
# положительных чисел.
# Записать его в файл построчно.


ls1 = set(int(i) for i in range(-5, 5))
with open("days.txt", "w") as f:
    for i in ls1:
        f.write(str(i) + "\n")
print(type(ls1))

# Прочитать предыдущий файл,
# сформировать из него
# множество, распечатать его.
lst = set()
with open("text.txt", "r") as f:
    for line in f:
        num = int(line)
        lst = lst.union({num})
print(lst)
print(type(lst))

# Пользователь вводит слова.
# Записать их в файл: каждое
# слово на отдельной строке
#
# Дан список [5, True, ‘abc’].
# Записать его в файл

text = [5, True, "abc"]
with open("days.txt", "w") as f:
    for i in text:
        f.write(str(i) + "\n")

# Создать список чисел. Записать
# каждое нечетное число в файл

import random

ls1 = [random.randint(0, 100) for i in range(10)]
with open("days.txt", "w") as f:
    for i in ls1:
        if i % 2 == 1:
            f.write(str(i) + "\n")