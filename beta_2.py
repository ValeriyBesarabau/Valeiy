# ЗАДАНИЕ № 1
str_1 = "rythm rough rush shake than"
str_2 = str_1.replace("a", "")
print(str_1)
print(len(str_1) - len(str_2))

# ЗАДАНИЕ № 2
str_1 = "rythm (rough rush shake) than"
print(str_1[0:5] + " " + str_1[25:29])

# ЗАДАНИЕ № 3
str_1 = "rythm rough rush shake than"
print(str_1.count("t"))

# ЗАДАНИЕ № 4
str_1 = "rythm rough rush shake than"
str_2 = str_1[0:3]
str_3 = str_1[25:27]
str_4 = str_1[::-1]
str_5 = str_4[-25:-4]
str_6 = (str_2 + " " + str_5 + " " + str_3)
print(str_5)

# ЗАДАНИЕ № 5
str_1 = "rythm rough rush shake than"
str_2 = str_1[6:23]
str_3 = str_2.replace("h", "H")
str_4 = (str_1[0:5] + " " + str_3 + str_1[23:27])
print(str_4)