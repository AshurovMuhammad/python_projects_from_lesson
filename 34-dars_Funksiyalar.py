# Funksiyalar

# def hello(name, word):    # argument
#     print("Hello ", name, ". Say ", word, sep="")
#
#
# hello("Anvar", "nma gap")     # parametrlar
# hello("Mike", "salom")


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(5, 10)
# get_sum('Salom ', 'Mike')


# Foydalanuvchi kiritgan 2 malumotni ketma-ket tarzda n marotaba konsolga chiqarib beradi
# def exaple(n, a, b):
#     s = ''
#     for i in range(n):
#         if i % 2 == 0:
#             s += a
#         else:
#             s += b
#     print(s)


# def three_on(n, a, b):
#     counter = 0
#     while counter != n:
#         if counter % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#         counter += 1


# def three_on(n, a, b):
#     for i in range(n):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# three_on(6, "+", "-")
# three_on(5, "0", "X")


# def maximum(one, two):
#     if one > two:
#         return one
#     elif one < two:
#         return two
#     else:
#         return
#
#
# m = maximum(8, 8)
# print(m)


# def example(one, two):
#     if one > two:
#         return one*two
#     elif one < two:
#         return one+two
#     else:
#         return
#
#
# one = int(input("1-raqam: "))
# two = int(input("2-raqam: "))
# res = example(one, two)
# print('Natija:', res)


# 1dan 10gacha bo'lgan sonlar kubi
# def cube(a):
#     return a*a*a
#
#
# for i in range(1, 11):
#     print(i, 'kubi', cube(i))


# Fibonachi ketma ketligi
# def fibonachi(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#
#
# fibonachi(25)


# Foydalanuvchikiritgan ro'yxatni birinch va oxirgi elementlarini o'rnini almashtirib beradi
# def change(lst):
#     lst1 = []
#     lst2 = []
#     for i in range(len(lst)):
#         if i == 0:
#             lst2.append(lst[i])
#         elif i == len(lst) - 1:
#             lst1.insert(0, lst[i])
#         else:
#             lst1.append(lst[i])
#     lst1 = lst1 + lst2
#     return (lst1)

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     start = lst.pop()   # Oxirgi elementni saqlaydi
#     end = lst.pop(0)    # Birinchi elementni saqlaydi
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['o', 'l', 'm', 'a']))


# lst1 = [1, 5, 8, 4, 12]
# lst2 = []
# lst3 = []
# for i in range(len(lst1)):
#     if i == 0:
#         lst3.append(lst1[i])
#     elif i == len(lst1) - 1:
#         lst2.insert(0, lst1[i])
#     else:
#         lst2.append(lst1[i])
# lst2 = lst2 + lst3
# print(lst2)


# def pryam():
#     a = int(input("To'g'ri to'rtburchak tomonini kiriting: "))
#     b = int(input("To'g'ri to'rtburchak asosini kiriting: "))
#     result = a * b
#     return f"Yuzasi: {result}"
#
#
# def uchbur():
#     a = int(input("1-katet uzunligini kiriting: "))
#     b = int(input("1-katet uzunligini kiriting: "))
#     result = (a * b)/2
#     return f"Yuzasi: {result}"
#
#
# def ayl():
#     r = int(input("Aylana radiusini kiriting: "))
#     p = 3.14
#     result = (p * r)**2
#     return f"Yuzasi: {result}"
#
# print(pryam())
# print(uchbur())
# print(ayl())






