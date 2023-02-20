# Lambda funksiyasi
# def func(x, y):
#     return x + y
# print(func(4, 5))
#
# print((lambda x, y: x + y)(4, 5))
#
# func1 = lambda x, y: x + y
# print(func1(5, 6))
# print(func1('as', 'salom'))

# print((lambda x, y: (x**2) + (y**2))(2, 5))


# summ = lambda a=1, b=2, c=3: a+b+c
# print(summ())

# func = lambda *args: args
# print(func(1, 2, 3, 4, 5))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for i in c:
#     print(i('abc'))


# birhil vazifani bajaradigon uch xil funksiya
# def yo'li;
# def inc(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# f = inc(42)
# print(f(2))


# lambda - yo'li;
# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(2))


# lamda - yo'li;
# inc = (lambda n: (lambda x: n + x))
# obj = inc(42)
# print(obj(2))


# res = (lambda a: (lambda b: (lambda c: a + b + c)))
# print(res(2)(4)(6))


# lambda funksiyasini methodda qo'llash
# d = {'a': 10, 'b': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# print(list_d)


# lambd afunksiyasi orqali ro'yxat shakillantirish
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# res1 = a[0](12, 6), a[1](10, 6), a[2](4, 6), a[3](36, 6)
# res1 = list(res1)
# print(res1)


# Uyga vazifa
# players = [{'name': 'Anton', 'last name': 'Birokov', 'rating': 9},
#            {'name': 'Aleksey', 'last name': 'Bodnya', 'rating': 10},
#            {'name': 'Fedor', 'last name': 'Sidarov', 'rating': 4},
#            {'name': 'Mixail', 'last name': 'Semenov', 'rating': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: (lambda: print('Monday')),
#     2: (lambda: print('Tuesday')),
#     3: (lambda: print('Wednesday')),
#     4: (lambda: print('Thursday')),
#     5: (lambda: print('Friday')),
#     6: (lambda: print('Saturday')),
#     8: (lambda: print('Sunday'))
# }
#
# d[2]()


# Shakllarni yuzini topadigon lambda funksiya
# d = {
#     'Doyra': (lambda r: 3.14 * (r**2)),
#     'Torburchak': (lambda x, y: x * y),
#     'Trapesiya': (lambda a, b, h: (a + b)/2 * h)
# }
# print(d['Trapesiya'](7, 5, 3))


# print((lambda a, b: a if a > b else b)(15, 13))

# print((lambda x, y, z: min(x, y, z))(6, 2, 12))

# print((lambda x, y, z: x if (x <= y) and (y <= z) else (y if (y <= x) and (y <= z) else z))(16, 12, 8))