# Funksiya Modullar

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False

# Paro'lni yaroqli yoki yaroqsiz ekanligini tekshirib beradigon funksiya.
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Parol: ")    # Dastlab yuqoridegi funksiya ishledi, u True yoki False qiymatni qaytaradi     # 125KilOj
# if check_password(p):            # Qachonki funksiya True bo'lsa ushbu if bajariladi
#     print("Yaroqli parol.")
# else:                           # Funksiya False qiymatni qaytarsa
#     print("Yaroqsiz parol.")


# def get_sum(a=5, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(d=2))


# Foydalanuvchi parametrni kirimasa avtomatik qiymatni oladi
# def set_param(col=20, smv="-"):
#     if col != 20 or smv != "-":
#         return col * smv
#     else:
#         return col * smv
#
#
# print(set_param())


# Foydalanuvchi kiritgan username va passwordni tekshiradi
# def check_password(username, password, min_length=8, check_user=True):
#     if len(password) < min_length:
#         print("Parol o'ta qisqa!")
#         return False
#     elif check_user and username in password:
#         print("Paro'lda foydalanuvchi ismidan foydalanilgan.")
#         return False
#     else:
#         print(f"{username}, foydalanuvchi uchun paro'l muvofaqyatli tekshirldi.")
#         return True
#
#
# check_password("igor", "12345")
# check_password("igor", "12345igor")
# check_password("igor", "12345name")


# Funksiyaga kiritilgan raqamlarni juftlarini va toqlarini yigindisini xisoblab beradigon funksiya
# def digit_sum(num, even=True):
#     num = str(num)
#     res_j = 0
#     res_t = 0
#     if even:
#         for i in num:
#             i = int(i)
#             if i % 2 == 0:
#                 res_j = res_j + i
#         return res_j
#     else:
#         for i in num:
#             i = int(i)
#             if i % 2 == 1:
#                 res_t = res_t + i
#         return res_t


# def digit_sum(num, even=True):
#     s = 0
#     while num > 0:
#         res = num % 10
#         if even and res % 2 == 0:
#             s += res
#         elif not even and res % 2 != 0:
#             s += res
#         num //= 10
#     return s
#
#
# print("Juft sonlar yigindsi:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print(digit_sum(123456789547821364))
#
# print("Toq sonlar yigindsi:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def fnc(a, ls=None):
#     if ls is None:
#         ls = []
#     ls.append(a)
#     return ls
#
#
# print(fnc(2))
# print(fnc(5))
# print(fnc(8))


# int va str ma'lumot turlari o'zgarmedigon ma'lumot turlari xisoblanadi
# a = 5
# b = 5
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)   # id si orqali tenglaydi

# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)   # id si orqali tenglaydi


# ls1 = [1, 2, 3]
# ls2 = [1, 2, 3]
# print(id(ls1))
# print(id(ls2))
# print(ls1 == ls2)
# print(ls1 is ls2)   # id si orqali tenglaydi


# def add_number(n):
#     print("Funksiya ichida:", n, "=", id(n))
#     n += 1
#     print("Ortirilgandan kegin:", n, "=", id(n))


# x = 1
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))


# Kartejlar (tuple)
# lst = [10, 20, 30]
# tp = (10, 20, 30)
# print(lst.__sizeof__())     # Bayt
# print(tp.__sizeof__())      # Bayt


# a = (1, 2, 3, 4, 5)
# print(a)
# b = 1, 2, 3
# print(tuple(b))
# print(tuple((5, 6, 7)))
#
# t = (2,)
# print(type(t))


# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[2:4])

# List
# s1 = [int(input("-> ")) for i in range(1, 3)]
# print(s1)

# Tuple
# s1 = tuple(int(input("-> ")) for i in range(1, 3))
# print(s1)

# import random
# s1 = tuple(random.randint(0, 100) for i in range(10))
# print(s1)

# import random
# s1 = tuple(random.randint(0, 5000) for i in range(12))
# print(s1)

# Ikkini darajalarini kortej (tuple)ga olib beradi
# a1 = tuple(2**i for i in range(1, 13))
# print(a1)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# for i in t3:
#     if i == ' ':
#         continue
#     print(i, end=" ")







