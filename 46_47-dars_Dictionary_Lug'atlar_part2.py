# Dictionary ichida yana dictionaryni xosil qilib uni xarbir elamentini chiqarish
# d = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(d)
# for i in d:
#     print(i)
#     for y in d[i]:
#         print('\t', y, '->', d[i][y])


# d = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612
#     },
#     'Anne': {
#         'N': 5239,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859
#     },
#     'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451
#     }
# }
#
# for i in d:
#     print(i)
#     for y in d[i]:
#         print(y, ':', d[i][y])
#
# print()
#
# while True:
#     ask1 = input('Name: ')
#     if ask1 == 'John' or ask1 == 'Tom' or ask1 == 'Anne' or ask1 == 'Fiona':
#         ask2 = input('Region: ')
#         print(d[ask1][ask2])
#         ask3 = int(input('New value: '))
#         d[ask1][ask2] = ask3
#         print(d[ask1])
#     else:
#         continue


# d = {'bir': 1, 'ikki': 2, 'uch': 3, 'tort': 4}
# print(d)
# b = {value: key for key, value in d.items()}
# print(b)


# d = {'bir': 1, 'ikki': 2, 'uch': 3, 'tort': 4}
# count = 0
# res = dict()
# for i, j in d.items():
#     res[i] = j
#     count += 1
#     if count == 2:
#         break
# print(res)

# d = {'bir': 1, 'ikki': 2, 'uch': 3, 'tort': 4}
# b = {key: value for key, value in d.items() if value <= 2}
# print(b)


# Dictionary shaklida ro'yxat yaratish
# count = 1
# d = {k: input('Name: ') for k in range(1, 4)}
# print(d)


# y = int(input('-> '))
# s = [10, 20, 30, 40]
# d = {i: y for i in s}
# print(d)


# s = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 16, 60, "four", -20]
# res = dict()
# x = None
# for i in s:
#     if type(i) == str:
#         res[i] = []
#         x = i
#     else:
#         res[x].append(i)
# print(res)


# zip funksiyasi
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)


# a = ['Dec', 'Yan', 'Feb']
# b = [12, 1, 2]
# d = {k: v for k, v in zip(b, a)}
# print(d)


# zip list
# a = ['Dec', 'Yan', 'Feb']
# b = [12, 1, 2]
# ls = list(zip(a, b))
# print(ls)


# zip tuple
# a = ('Dec', 'Yan', 'Feb')
# b = (12, 1, 2)
# ls = tuple(zip(a, b))
# print(ls)


# a = {'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4, 'e1': 5}
# b = {'a2': 10, 'b2': 20, 'c2': 30, 'd2': 40, 'e2': 50}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)


# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)


# a = ['a', 'b', 'c', 'd']
# b = [1, 2, 3, 4]
# print(list(zip(a, b)))


# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, production_cost, month):
#     res = sales - cost
#     print(m, 'oyidegi umumiy kirim =', res)


# Ikki lug'atni birlashtirish /// albatta daftarga yozaman
# one = {'apple': 0.04, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})


#  enumerate function
# Ro'yxatdegi elementlarni enumerate funksiyasi yordamida raqamlash /// albatta daftarga yozaman
# colors = ['blue', 'black', 'yellow', 'green']
# for i, color in enumerate(colors, 1):
#     print(i, color)


# Lug'atdegi elementlarni enumerate funksiyasi yordamida raqamlash /// albatta daftarga yozaman
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for i, (k, v) in enumerate(d.items(), 5):
#     print(i, '->', k + ':', v)


# iter funksiyasi ushbu funksiya yordamida ro'yxatdegi elementlarni o'zimiz komanda orqali kerakli
# vaqda chiqarishimiz mumkin
# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(next(itr))
# print('Say hello')
# print(next(itr))
# print('Say bye')
# print(next(itr))






