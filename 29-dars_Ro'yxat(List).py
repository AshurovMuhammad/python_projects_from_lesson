# List
# nims = [1, 2, 3, 4, 5]
# print(type(nims))


# n1 = [0, 1, 2, 3, 4, 5]
# n2 = list(range(6))
# print(id(n1))
# print(id(n2))
# print(n1)
# print(n2)
# # Bu xolatda listni ichidagi qiymati bo'yicha taqqoslanadi
# if n1 == n2:
#     print("Qiymat teng")
# else:
#     print('Qiymat teng emas')
#
# # Bu xoldagi solishtirish yani 'is' yordamida, ro'yxatni id qiymati bo'yicha taqqosledi
# if n1 is n2:
#     print("Qiymat teng")
# else:
#     print('Qiymat teng emas')


# n = 5
# a = [i**2 for i in range(1, n)]
# print(a)


# a = [5, 8, 9, 7]
# b = [2, 3, 1]
# c = b + a
# print(c)


# Foydalanuvchidan so'rab ro'yxatni shakillantirish
# a = [0] * int(input("Ro'yxatdegi elementlar sonini kiriting: "))
# print(a)
# counter = 1
# for i in range(len(a)):
#     a[i] = int(input(f"{counter}- elementni kiriting: "))
#     counter += 1
# print(a)

# a = [int(input("Raqam: ")) for i in range(int(input("Nechta raqam kiritmoqchisiz: ")))]
# print(a)
#
# a = [input("Talabaning ismi: ") for i in range(int(input("Nechta talaba mavjud: ")))]
# print(a)


# Ro'yxatga kiritilgan manfiy sonlar yig'indisini xisoblash
# a = [0] * int(input("Ro'yxatdegi elementlar sonini kiriting: "))
# sum = 0
# counter = 1
# for i in range(len(a)):
#     a[i] = int(input(f"{counter}-raqamni kiriting: "))
#     if a[i] < 0:
#         sum = sum + a[i]
#     counter += 1
# print("Ro'yxatdegi elementlar: ", a)
# print("Manfiy sonlar yig'indisi:", sum)


# Ro'yxatdegi juft sonlar sonini va ro'yxatdegi toq sonlar yig'ndisini topib beradi
# list1 = list(range(21, 41))
# print(list1)
# couter_juft = 0
# sum = 0
# for i in list1:
#     if i % 2 == 0:
#         couter_juft += 1
#     if i % 2 != 0:
#         sum = sum + i
# print("Ro'yxatdegi juft sonlar:", couter_juft)
# print("Ro'yxatdegi toq sonlar yigindisi:", sum)


# Foydalanuvchi xosil qilgan ro'yxat elementlarini o'rta arifmetigini topadi,
# agar ro'yxatda 0 raqami bo'lsa uni xisobga olmedi
# a = [int(input("--> ")) for i in range(int(input("n: ")))]
# s = k = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         k += 1
# print("O'rta arifmetigi:", s/k)


# Ro'yxadni qirqib olish (срез)
# Formula: list[start:stop:step]
# s = list(range(1, 8)) # [1, 2, 3, 4, 5, 6, 7]
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])





