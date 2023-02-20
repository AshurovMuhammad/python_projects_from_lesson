# Ro'yxat methodlari
# s = [1, 2, 4, 8, 6, 5, 7, 3, 2, 4]
# print(s)
# s.append(22)
# print(s)
# s.extend([33, 44, 55])
# print(s)
# b = []
# for i in range(len(s)):
#     if s[i] not in b:
#         b.append(s[i])
# print(b)
# print(s)

# list1 = list(range(1, 11))
# list2 = []
# for i in range(len(list1)):
#     list2.extend([list1[i]**2])
# print(list2)

# s = [1, 2, 4, 8, 6, 5, 7, 3, 2, 4]
# s.insert(1, 10)
# print(s)


# Foydalanuvchi kiritgan sonni 3ga qoldiqsiz bo'linadiganlarini ro'yxatini xosil qiladi
# lst = []
# n = int(input("Ro'yxatdegi elementlar soni: "))
# count = 1
# for num in range(n):
#     x = int(input(f"{count}-raqamni kiriting: "))
#     if x % 3 == 0:
#         lst.append(x)
#     else:
#         print(f"{x} raqam 3ga qoldiqsiz bo'linmedi")
#     count += 1
# print(lst)

# Ikki ro'yxatdegi elementlarni taqqoslash, aga bir ro'yxatta birxil element 2tadan ko'p bo'lsaha 1 donadan oladi
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
# print(c)


# Ikki ro'yxatni ketma- ketlikda yangi ro'yxatga joylash
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in a:
#     for j in b:
#         if i == j % 10:
#             c.extend([i, j])
# print(c)


# s = [1, 5, 6, 8, 2, 5, 7, 6, 1]
# print(s)
# s.remove(7)  # Remove methodi parametri sifatida ro'yxatdegi qiymatni o'zini oladi
# last = s.pop(2)   # pop methodi parametri sifatida ro'yhatdegi qiymatni index
# print(last)       # raqamini oladi va ushbu index ostidegi qiymatnixam saqlab qoladi
# s.reverse()
# s.clear()
# del s[:]
# print(s)


# Foydalanuvchi shakillantirgan ro'yxatni elementlarini indexi orqali o'chirish
# a = [int(input("--> ")) for i in range(int(input("n: ")))]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
# print(c)
# a2 = int(input("Indexni kiriting: "))
# c.pop(a2)
# print(c)


# Ro'yxatdegi elementlarni yagonalarini aniglab beradi yani bitta element 2, 3 marta kelhan bo'sa qabul qilmedi
# s = [1, 4, 8, 7, 3, 5, 6, 8, 2, 5, 7, 6, 1]
# print(s)
# for i in s:
#     if s.count(i) == 1:
#         print(i, end=" ")

# Ro'yxatdegi elementlarni hariflari soniga qarab sartarofka qilib beradi
# name = ["Muhammad", "Dilmurod", "Ali", "Hasan"]
# name.sort(key=len)
# print(name)

# s = [1, 5, 6, 8, 2, 5, 7, 6, 1]
# print(s)
# num = s.count(1)
# print(num)
# print(s)




