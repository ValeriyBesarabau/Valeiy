# def sum_list(list_num):
#     summ = 0
#     while list_num != 0:
#         summ += int(list_num) % 10
#         list_num = list_num // 10
#     return summ
# for i in sorted([965, 582, 23, 8, 695210]):
#     print(sum_list(i))



# def f(x):
#     if x <= -2: f = 1 - (x + 2)**2
#     elif -2 < x <= 2: f =- (x / 2)
#     elif x > 2: f = (x - 2)**2 + 1
#     return f
#
#
# print(f(4.5))



# def modify_list(l):
#     num = []
#     for i in l:
#         if i % 2 == 0:
#             num.append(i // 2)
#     return num
# numbers = (int(i) for i in input().split())
#
#
# print(modify_list(numbers))
