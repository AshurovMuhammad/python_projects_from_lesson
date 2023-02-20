# Matritsa va Modullar
import locale
import random as r

# Matritsa yaratish
# w, h = 5, 4
# matrix = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
# # matrix = []
# # for y in range(h):
# #     n = []
# #     for x in range(w):
# #         n.append(r.randint(1, 30))
# #     matrix.extend([n])
# print(matrix)
#
#
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()


# Matritsadegi manfiy sonlar sonini aniqlab beradi
# w, h = 3, 4
# matrix = [[r.randint(-20, 10)for x in range(w)] for y in range(4)]
# print(matrix)
# minus = 0
# for h in matrix:
#     for w in h:
#         if w < 0:
#             minus += 1
#         print(w, end="\t\t")
#     print()
# print("Manfiy raqamlar:", minus)


# Matritsadegi sonlar ko'paytmasini aniqlab beradi
# w, h = 3, 4
# matrix = [[r.randint(0, 4)for x in range(w)] for y in range(4)]
# print(matrix)
# pro = 1
# for h in matrix:
#     for w in h:
#         if w != 0:
#             pro = pro * w
#         print(w, end="\t\t")
#     print()
# print("Sonlarni umumiy ko'paytmasi:", pro)


# w, h = 6, 6
# matrix = [[r.randint(0, 10) for x in range(w)] for y in range(4)]
# print(matrix)
# matrix2 = []
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()
# for h in matrix:
#     if matrix.index(h) == 0:
#         matrix2.insert(1, h)
#     elif matrix.index(h) == 1:
#         matrix2.insert(0, h)
#     elif matrix.index(h) == 2:
#         matrix2.insert(3, h)
#     elif matrix.index(h) == 3:
#         matrix2.insert(2, h)
#
# for h in matrix2:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()


# lst = [1, 2, 3, 4]
# lst2 = []
# for n in lst:
#     if n % 2 == 0:
#         lst2.append(n)
#         lst2.append(n-1)
# print(lst2)


# lst = [1, [1, 2, 3], 56, [78, 85, 96, 74, 2], 6, 8]
# print(lst[3])
# se = [5, 6, 4]
# lst.extend([se])
# print(lst)


# 1  2  3  4  5
# 8  9  10 11 12
# 15 16 17 18 19
# 22 23 24 25 26
# 29 30 31

# days = [d for d in range(1, 32)]
# print(days)
# weeks = [days[i:i+5] for i in range(0, len(days), 7)]
# print(weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()


import math
import time
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime(seconds)
# print(local_time)
#
# res = time.localtime(seconds)   # tm_wday >> week days, dushamba = 0 seshanba = 1 .....
# print(res)                      # tm_yday >> year days, 0, 1, 2, 3 ...... 365
# print(res.tm_yday)
#
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 5
# print("Program is started ...")
# time.sleep(pause)
# print(pause, 'second.')


# text = input("Nimani eslatib qo'ye? > ")
# t = float(input("Qancha minutdan kegin? > "))
# t *= 60
# time.sleep(t)
# print(text)


# locale.setlocale(locale.LC_ALL, "uz")
# print(time.strftime("Bugun %B %d %Y"))
# print(time.ctime())








