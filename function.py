# def sum_list(list_num):
#     """Из полученного списка чисел
#         создайте список с суммами
#         этих чисел, отсортированными
#         по возрастанию:
#         In: 965 582 023 8 695210
#         Out: [5, 8, 15, 20, 23]"""
#     summ = 0
#     while list_num > 0:
#         summ += list_num % 10
#         list_num = list_num // 10
#     return summ
# for i in sorted([965, 582, 23, 8, 695210]):
#     print(sum_list(i))





# def f(x):
#     """Напишите функцию f(x), которая
#         возвращает значение следующей
#         функции, определённой на всей
#         числовой прямой:
#         In: 4.5
#         Out: 7.25"""
#     if x <= -2: f = 1 - (x + 2)**2
#     elif -2 < x <= 2: f =- (x / 2)
#     elif x > 2: f = (x - 2)**2 + 1
#     return f
#
#
# print(f(4.5))
#
#
#
# def modify_list(l):
#     """Напишите функцию которая
#         принимает на вход список
#         целых чисел, удаляет из него
#         все нечётные значения, а
#         чётные нацело делит на два.
#         In: 852 85 784 58
#         Out: [852, 784, 58]"""
#     num = []
#     for i in l:
#         if i % 2 == 0:
#             num.append(i // 2)
#     return num
# numbers = (int(i) for i in input().split())
#
#
# print(modify_list(numbers))
