# Funksiyadegi lokal va global o'zgaruvchilar

# Lifehack
# a = [1, 2, 3]
# b = [a, 5, 6, 7]
# print(b)

# a = [1, 2, 3]
# b = [*a, 5, 6, 7]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1, 'salom', 5))


# def summa(*param):
#     res = 0
#     for n in param:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4))


# Funksiyaga kiritilgan ma'lumotlarni lugat ko'rinishda qaytaradi
# def func(*a):
#     return {i: i for i in a}
#
#
# print(func(1, 2, 3, 4))
# print(func('gray', (2, 17), 3.11, -4))


# Bu funksiya kiritilgan qiymatlarni o'rta arifmedigini topib, o'sha qiymatdan kichkinalarini aniglab beradi
# def func(*num):
#     arf = sum(num)/len(num)
#     ls = []
#     for i in num:
#         if i < arf:
#             ls.append(i)
#     print(arf)
#     return ls
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, 'salom'))


# def func(student, *scores):
#     a = "Talabaning ismi: " + student
#     s = []
#     for score in scores:
#         s.append(score)
#     print(a, end=" ")
#     print(*s, sep=", ")
#
#
# (func("Igor", 100, 95, 88, 92, 99))
# (func("Rick", 69, 96, 88, 20, 33))


# Funksiya yordamida kiritilgan qiymatni teskari (123:321) xolda qaytaradi
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


# Foydalanuvchi haqidagi malumotni lug'at ko'rinishda chiqarib beradi
# def into(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
#
# into(firstname='Muhammad', lastname='Ashurov', age=22, phone='1122334455')
# into(firstname='Ali', lastname='Muradov', email='respect@gmail.com', age=22, phone='1122334455', country='Andijon')


# Lifehack
# def db(**data):
#     my_dict.update(**data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='gray')
# print("my_dict =", my_dict)


# Yodda tuting!!!           * -> positsionniy argumenti,   ** -> imenovanniye argumenti
# def func(a, *args, b=False, **kwargs):
#     return a, args, b, kwargs
#
#
# print(func(1, 2, 3, 4, b=True, x=11, y=12, z=13))


# def func(*args):
#     print(args[0])
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
# func(1, 2, 3, 4)
# func2(one=123, two=456)


# Lifehack
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)


# scape - Kirish maydoni (область видимости) Pythonda 4ta
# если переменная создана за пределлами допустим функции то это будет глобалная
# name = "Tom"    # global o'zgaruvchi
#
#
# def hi():
#     global name
#     name = "Sam"    # lokal o'zgaruvchilar
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()


# i = 5
#
#
# def func(arg=i):
#     return arg
#
#
# i = 6
# print(func())

# def add_two(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return x + a
#     return add_some()
#
#
# print(add_two(3))


# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)


# def outer(echo):
#     def inner_func():
#         print("Hello", echo)
#     inner_func()
#
#
# outer('World')


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print('Ichki funksiya natijasi:', a + b)
#     print('Tashqi funksiya qiymati:', a)
#     fun2(10)
#
# fun1()


# Geometrik shakillarni yuzalarini aniqlaydigon dastur
# import math
#
#
# def func(figur_name, **kwargs):
#     if figur_name == 'romb':
#         return kwargs['d1'] * kwargs['d2']/2
#     elif figur_name == 'kvadrat':
#         return kwargs['c']**2
#     elif figur_name == 'trapetsiya':
#         return (kwargs['a'] + kwargs['b'])/2 * kwargs['h']
#     elif figur_name == 'doyra':
#         return math.pi * kwargs['r']**2
#
#
# print(func(figur_name='romb', d1=10, d2=8))
# print(func(figur_name='kvadrat', c=5))
# print(func(figur_name='trapetsiya', a=12, b=3, h=6))
# print(func(figur_name='doyra', r=18))


# def func(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(func(2, 3, 1, 4))


# To'gri burchakli paralelopipedni yuzasini topish, ichida esa to'g'ri to'rtburchak yuzini topadigon funksiyasi bilan
# Usul-1: lokal o'zgaruvchi yo'li bilan
# def rect_parel_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#
#
# print(rect_parel_square(2, 4, 6))
# print(rect_parel_square(5, 8, 2))
# print(rect_parel_square(1, 6, 8))

# Usul-2: global o'zgaruvchi yo'li bilan
# s = 0
#
#
# def rect_parel_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#
#
# print(rect_parel_square(2, 4, 6))
# print(s)
# print(rect_parel_square(5, 8, 2))
# print(s)
# print(rect_parel_square(1, 6, 8))
# print(s)

# Usul-3: local bo'lmagan o'zgaruvchi yo'li bilan
# def rect_parel_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
#
#
# print(rect_parel_square(2, 4, 6))
# print(rect_parel_square(5, 8, 2))
# print(rect_parel_square(1, 6, 8))


# Zamikaniya   //  Tutashuv
# def func(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# print(func(5)(10))
#
# add5 = func(5)
# print(add5(10))
# print(add5(6))
#
# add6 = func(6)
# print(add6(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + ' map'
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# print(func1()())
# func = func1()
# print(func())


# Shaxarlarga borganini sanab beadigon funksiya
# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res = func('Toshkent')
# res()
# res()
#
# res2 = func('Andijon')
# res2()
# res2()
# res()


# Talabalarni ballari oraligi bo'yicha lugatga joylab beradigon funksiya
# students = {
#     'Alise': 98,
#     'Bob': 67,
#     'David': 85,
#     'Chris': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v < upper}
#     return inner
#
#
# a = outer(80, 100)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# Funksiya ichidegi yana bir nechta funksiyalarni chaqirish
# def func_object(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def nul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.nul = nul
#
#     return replace
#
#
# obj1 = func_object(5, 2)
# print(obj1.add())
# obj2 = func_object(5, 2)
# print(obj2.sub())
# obj3 = func_object(5, 2)
# print(obj3.nul())




