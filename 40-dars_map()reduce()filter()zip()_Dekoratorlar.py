# map() reduce() filter() zip() funksiyalari. Dekoratorlar

# map(func, iterable)    // iterable objects -> bu, biz ushbu malumotlar ustida amallarqilishimiz mumkin bo'ladi

# def nul(t):
#     return t * 2
#
#
# s = 'Hello'            # [2, 4, 6, 8, 12]
# res = list(map(nul, s))     # tuple, set, list
# print(res)


# s = (2, 5, 10, 8)
# print(list(map(lambda t: t*2, s)))


# s = ['1', '2', '3', '4', '5']
# print(list(map(int, s)))


# areas = [3.45654, 5.57458, 4.5665652, 56.656556, 9.015445]
# res = list(map(round, areas))
# print(res)


# Ikki ro'yxat elementlarini qo'shib beradi
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# import random
# lst = [random.randint(0, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda x: x >= 10 and x <= 20, lst))
# print(res)


# Ro'yxatdegi 15ga bo'linadigon sonlarni filter funksiyasi yordamida filterlash
# lst = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, lst))
# res2 = list(filter(lambda s: not s % 15, lst))
# print(res)
# print(res2)


# map va filter funksiyalari yordamida 1 dan 10 gacha bo'lgan toq raqamlarni kvadratlarini chiqarish
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 !=0, range(10)))))      # 1-usul
# print([x ** 2 for x in range(10) if x % 2 != 0])        # 2-usul


# ro'yxatni tekshirib polidrom so'zlarni aniqlab beradi, (madam -> madam)
# s = ['madam', 'fire', 'tomato', 'book', 'mom']
# print(s)
# print(list(filter(lambda x: x[::-1] == x, s)))


# Dekaratorlar

# def hello():
#     return "Hello, I am func 'hello'"


# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):     # декорируещая функция
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# @my_decorator       # декоратор
# def func_test():        # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print('Hello')
#
#
# func_test()
# hello()
# test = my_decorator(func_test)
# test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         fn()
#         print('Chaqirishlar soni:', count)
#     return inner
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Malumotlar", arg1, arg2)
#         fn(arg1, arg2)
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Mening ismim", first, last)
#
#
# print_full_name('Muhammad', 'Ashurov')
# def my_dec(fn):
#     def inner(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#     return inner
#
#
# @my_dec
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, "o'qiydi", study, '\n')
#
#
# print_full_name('Ashurov', 'Muhammad', 'Ravshanbekovich', study='Java')
# print_full_name('Nazarov', 'Ali', 'Sobirovich')


def dec_func(arg1, arg2):
    print('Argumentlari:', arg1, arg2)

    def wrapper(func1):

        def wrap(func_arg1, func_arg2):
            print('Funksiya argumentlari:', func_arg1, func_arg2)
            func1(func_arg1, func_arg2)
            func1(arg1, arg2)

        return wrap

    return wrapper


@dec_func('Iqbol', 'Komolov')
def func(first, last):
    print('Mening ismim: ', first, last)


func('Ashurov', 'Muhammd')


# def args_decorator(decorator_text):
#     def wrapper(func):
#         def wrap(a):
#             print(decorator_text, end='')
#             func(a)
#
#         return wrap
#     return wrapper
#
#
# @args_decorator(decorator_text='Hello ')
# def hello_world(text):
#     print(text)
#
#
# hello_world('world!')


# def dec_nul(num2):
#     def wrapper(func):
#         def wrap(num):
#             print('Result:', num2 * func(num))
#
#         return wrap
#     return wrapper
#
#
# @dec_nul(3)
# def numm(num1):
#     return num1
#
#
# numm(5)


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*fn_args, **fn_kwargs):
#             for i in range(len(args)):
#                 if type(fn_args[i]) != args[i]:
#                     raise TypeError("Noaniq malumot turini kiritdingiz!")
#             return fn(*fn_args, **fn_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Hello'))
# print(typed_fn2('Hello ', 'world', '!'))


# def decor(tx=None, dec_text=""):
#     def wrapper(func):
#         def wrap(*args):
#             print(dec_text, end='')
#             func(*args)
#         return wrap
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# hello_world2('Hi!')
#
#
# @decor(dec_text='Hello ')
# def hello_world(text):
#     print(text)
#
#
# hello_world('world!')







