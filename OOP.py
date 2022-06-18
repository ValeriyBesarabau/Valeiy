# Создать класс Dog.
# Класс имеет четыре
# атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый
# метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все
# методы
# объекта и вывести на экран все его
# атрибуты.

# class Dog:
#     color = "Локи черного цвета"
#     character = "Очень дружелюбная"
#
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#
#     def jump(self, m):
#         return f"Собака {self.name} подпрыгивает в высоту на {m} метра"
#
#
#     def run(self, c):
#         return f"Собака {self.name} бежит со скоростью {c} м/с"
#
#
#     def bark(self, bark):
#         return f"Собака {self.name} {bark} лает"
#
#
# sheep_dog = Dog(1.5, 60, "Локи", 6)
#
# print(sheep_dog.color)
# print(sheep_dog.character)
# print(sheep_dog.jump(3))
# print(sheep_dog.run(10))
# print(sheep_dog.bark("громко"))
# print(sheep_dog.__dict__)


# Добавить в класс Dog метод change_name.
# Метод
# принимает на вход новое имя и меняет
# атрибут имени у
# объекта. Создать один объект класса.
# Вывести имя.
# Вызвать метод change_name. Вывести имя.

# class Dog:
#
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#
#     def jump(self, m):
#         return f"Собака {self.name} подпрыгивает в высоту на {m} метра"
#
#
#     def run(self, c):
#         return f"Собака {self.name} бежит со скоростью {c} м/с"
#
#
#     def bark(self, bark):
#         return f"Собака {self.name} {bark} лает"
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#
# sheep_dog = Dog(1.5, 60, "Локи", 6)
# sheep_dog.name = "пушок"
#
#
#
# print(sheep_dog.jump(3))
# print(sheep_dog.run(10))
# print(sheep_dog.bark("громко"))
# print(sheep_dog.__dict__)
# print(sheep_dog.name)
