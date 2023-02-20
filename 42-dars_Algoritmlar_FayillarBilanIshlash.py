# bubble algoritmi / Sonlarni tartiblash

# Tasodifiy ro'yxatni shakillantirib uni bubble algoritmi yordamida o'sish tartibi bo'yicha joylashtirib beradi.
# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - 1 - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)


# Tasodifiy ro'yxatni shakillantirib uni bubble algoritmi yordamida kamayish tartibi bo'yicha joylashtirib beradi.
# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)


# def kamayish(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# def osish(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - 1 - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a, b, c, d = [5, 9, 6, 7], [3, 11, 8], [2, 4], [10, 1, 12]
# lst = a + b + c + d
#
# ask = int(input("1 - kamayish tartibi bo'yicha\n2 - o'sish tartibi bo'yicha\n-> "))
# if ask == 1:
#     kamayish(lst)
#     print(lst)
#     ask2 = int(input('Qidirayotgan raqamingizni kiriting: '))
#     if ask2 in lst:
#         print('Raqam', ask2, 'topildi ☺')
#     else:
#         print(ask2, "topilmadi")
# elif ask == 2:
#     osish(lst)
#     print(lst)
#     ask2 = int(input('Qidirayotgan raqamingizni kiriting: '))
#     if ask2 in lst:
#         print('Raqam', ask2, 'topildi ☺')
#     else:
#         print(ask2, "topilmadi")
# else:
#     print('Error!!!')


# marge sort algoritmi
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
# a = [2, 4, 5, 9, 12, 3, 15, 0]
# print(a)
# print(marge_sort(a))


# shell sort algoritmi
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
# s = [10, 44, 26, 14, 67, 21, 9, 87]
# print(s)
# res = shell_sort(s)
# print(res)


# Fayllar bilan ishlash
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(*f)
# print(f)


f = open('test.txt', 'r')
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines())


# count = 0
# for line in f:
#     count += 1
#
# print('Line', count)
# f.close()


# f = open('xyz.txt', 'a')
# lst = ['\nsalom\n', 'ali\n', 'nma gap']
# f.writelines(lst)
