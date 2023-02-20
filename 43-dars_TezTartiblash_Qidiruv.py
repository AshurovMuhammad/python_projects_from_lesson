# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))
# print(seq_search(lst, 32))


# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found


# lst = [1, 2, 8, 17, 19, 42]
# print(binary_search(lst, 3))
# print(binary_search(lst, 8))


# from random import randint
#
# lst = sorted([randint(1, 99) for i in range(10)])
# print(lst)
# ask = int(input('Raqam kiriting: '))
#
#
# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     if found:
#         print(ask, "ro'yxatda mavjud ☺")
#     else:
#         print(ask, "ro'yxatda mavjud emas.")
#
#
# binary_search(lst, ask)


# Tartiblash
# bubble sort o'sish tartibi bo'yicha   / result: 7.859 sec
# import time as t
# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10000)]
# print(a)
# start = t.monotonic()
# bubble(a)
# print(a)
# finish = t.monotonic() - start
# print(round(finish, 3), 'sec')


# bubble sort kamayish tartibi bo'yicha
# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)


# marge sort algoritmi     /  result: 0.047 sec
# import time as t
# import random as r
#
#
# def marge_sort(a):
#     n = len(a)
#
#     if n < 2:
#         return a
#
#     l = marge_sort(a[:n // 2])
#     r = marge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# a = [r.randint(1, 99) for i in range(10000)]
# print(a)
# start = t.monotonic()
# array = marge_sort(a)
# print(array)
# finish = t.monotonic() - start
# print(round(finish, 3), 'sec')


# shell sort algoritmi     /  result: 0.031 sec
# import time as t
# import random as r
#
#
# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pas = val
#
#             while pas >= gap and s[pas - gap] > cur_val:
#                 s[pas] = s[pas - gap]
#                 pas -= gap
#                 s[pas] = cur_val
#
#         gap //= 2
#     return s
#
#
# s = [r.randint(1, 99) for i in range(10000)]
# print(s)
# start = t.monotonic()
# res = shell_sort(s)
# print(res)
# finish = t.monotonic() - start
# print(round(finish, 3), 'sec')

