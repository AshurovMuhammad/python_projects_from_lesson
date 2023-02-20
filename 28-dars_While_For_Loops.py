# while loop

# i = 2
# while i <= 10:
#     print("i =", i)
#     i += 2

# num = int(input("Raqam: "))
# while num > 0:
#     print("*", end="")
#     num -= 1

# num1 = int(input("Raqam 1: "))
# num2 = int(input("Raqam 2: "))
# sum = 0
# while num1 <= num2:
#     if num1 % 2 != 0:
#         sum = sum + num1
#     num1 = num1 + 1
# print(sum)

# a = int(input("Raqam: "))
# b = 0
# c = 0
# ans = a
# while a > 0:
#     b = a % 10
#     c = c * 10 + b
#     a = a // 10
#
# if c == ans:
#     print(ans, "- palidron raqam")
# else:
#     print(ans, "- palidron raqam emas")
#
# print(ans, "- palidron raqam", (" " if c == ans else "emas"),)

# kol = int(input("Nechta raqam kiritmoqchisiz: "))
# count_kol = 1
# count_ch = 1
# ch = float(input(f"{count_ch}-raqamni kiriting: "))
# sum_ch = ch
# min_ch = ch
# max_ch = ch
# while kol > count_kol:
#     ch = float(input(f"{count_ch+1}-raqamni kiriting: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     count_kol += 1
#     count_ch += 1
# arifmetigi = sum_ch / kol
# print("O'rta arifmetifi >", arifmetigi)
# print("Minimal >", min_ch)
# print("Maximal >", max_ch)

# num = input("Butun son kiriting: ")
# while type(num) != int:
#     try:
#         num = int(num)
#     except ValueError:
#         print("Butun raqam kiritmadingiz!")
#         num = input("Butun son kiriting: ")
# if num % 2 == 0:
#     print(num, "juft son")
# else:
#     print(num, "toq son")
# =======================================================================================================================

# while // continue, break

# while True:
#     n = int(input("Musbat raqam kiriting: "))
#     if not n > 0:   # if n < 0:
#         break


# Ko'paytirish jadvali
# i = 1
# while i < 10:
#     b = 1
#     while b < 10:
#         result = b * i
#         print(f"{b} * {i} = {result}", end='\t\t')
#         b += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end="")
#         j += 1
#     print()
#     i += 1

# Yoz
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print('^', end="")
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, '*')
#     i += 1

# Yoz
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for loop

# i = 1
# for color in 'red', 'yellow', 'black', True, 5, 2.2:
#     print(i, 'color:', color)
#     i += 1

# Yoz
# for i in range(10):
#     print(i, end=' ')
# print()
# for i in range(1, 9, 3):
#     print(i, end=' ')
# print()
# for i in range(9, 0, -1):
#     print(i, end=' ')
# print()
# for i in range(100, 0, -10):
#     print(i, end=' ')
# print()


# Foydalanuvchi kiritgan raqamni qoldiqsiz bo'linuvchilarini aniqlab beradi
# num = int(input("Raqam: "))
# for i in range(1, num):
#     if num % i == 0:
#         print(i, end=" ")
# print()

# 1 dan 100 gacga bo'lgan juft honali raqamlarni chiqarib beradi
# c = 1
# for i in range(10, 100, 10):
#     i = i + c
#     c += 1
#     print(i, end=" ")
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# w = int(input("Width: "))
# h = int(input("Height: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h-1 or j == 0 or j == w-1:
#             print('*', end='')
#         else:
#             print(' ', end="")
#     print()


# print([i for i in range(10) if i % 2 == 0])
# print([letter * 2 for letter in "Banana"])


