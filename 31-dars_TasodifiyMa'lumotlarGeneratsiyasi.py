# Tsodifiy ma'lumotlar grnrratsiaysi
import random as r

# choice
# city_list = ['Andijon', 'Toshkent', 'Namangan', 'Buxoro', 'Xiva']
# print(r.choice(city_list))

# choices
# lst = [10, 55, 20, 45, 12, 78, 96, 65, 78, 74, 32, 0]
# print(r.choices(lst, k=4))

# shuffle
# lst2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# r.shuffle(lst2)
# print(lst2)

# uniform
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))


# lst3 = [i for i in range(10)]
# print(lst3)
#
# # Tasidifiy raqamlar generatsiyasi
# lst4 = [r.randint(1, 100) for i in range(10)]
# print(lst4)


# Ro'yxatdegi eng katta sonni olib uni ro'yxatni eng boshiga qo'yib beradi
# list5 = [5, 16, 20, 45, 2, 4, 7, 9, 100]
# print(list5)
# print(max(list5))
# a = max(list5)
# for i in list5:
#     if i == a:
#         list5.remove(a)
#         list5.insert(0, i)
# print(list5)


# Ro'yxatdegi eng kichik qiymatni aniglab undan kegingi qiymatlarni chiqaradi
# list6 = [r.randint(0, 100) for i in range(10)]
# m = min(list6)
# for i in list6:
#     if i == m:
#         print(list6)
#         print("Min:", m)
#         print("Index min:", list6.index(i))
#         print(list6[list6.index(i):])


# n1 = 5
# n2 = 4
# l1 = [r.randint(0, 10) for i in range(n1)]
# l2 = [r.randint(0, 10) for j in range(n2)]
# l3 = l1 + l2
# list3 = []
# list4 = []
# for list1 in l1:
#     if list1 not in l2:
#         continue
#     else:
#         list3.append(list1)
# for list1 in l1:
#     if list1 in l2:
#         continue
#     else:
#         list4.append(list1)
# for list2 in l2:
#     if list2 in l1:
#         continue
#     else:
#         list4.append(list2)
# print(l1)
# print(l2)
# print(l3)
# print(list3)
# print(list4)
# c = [max(l1), max(l2), max(l3)]
# print(c)


# Tasodifiy raqamlar ro'yxati / for, while varianti
# num = int(input("Raqam: "))
# a = list()
# for i in range(num):
#     n = r.randint(0, 9)
#     if n not in a:
#         a.extend([n])
# print(a)

# num = int(input("Raqam: "))
# a = list()
# while len(a) != num:
#     n = r.randint(0, 9)
#     if n not in a:
#         a.extend([n])
# print(a)


# s = [2, 3]
# s.extend([5])
# print(s)

