# class NegativeNumber(Exception):
#     def __init__(self, text, number):
#         self.text = text
#         self.number = number
#
# class Pet:
#
#     def __init__(self, dog, cat, parrot):
#         self.dog = dog
#         self.cat = cat
#         self.parrot = parrot
#         self.name = None
#
# 
#     def set_parrot(self, number):
#         if number <= 0:
#             raise NegativeNumber("Число не может быть отрицательным или равно нулю")
#         self.parrot = number
#
#     def set_name(self, text):
#         if text == "":
#             raise NegativeNumber("Должно быть имя")
#         self.name = text
#
#
# b = Pet(10, 12, 7)
# b.set_parrot(5)
# print("У нас есть", b.parrot, "попугаев")
# b.set_name("Цветастик")
# print("Одного из них зовут", b.name)