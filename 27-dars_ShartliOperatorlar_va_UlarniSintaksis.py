#  Shartli operatorlar

# res = int(input("0dan 9 gacga raqam kiriting: "))
# if res == 1:
#     print('vorona')
# elif res == 2 or res == 3 or res == 4:
#     print('voronы')
# elif res == 5 or res == 6 or res == 7 or res == 8 or res == 9 or res == 0:
#     print('voron')
# else:
#     print("Xato malumot kiritildi!!!")

# res = int(input("1dan 99 gacga raqam kiriting: "))
# check = res
# if 11 <= check <= 14:
#     print(res, 'kopeek')
# else:
#     check = check % 10
#     if check == 1:
#         print(res, 'kopeyka')
#     elif 2 <= check <= 4:
#         print(res, 'kopeyki')
#     else:
#         print(res, 'kopeek')

# Shartlarni bir qatorga yozish yani (тернарное ввыражение) uchlik tekshirish
#  TRUE if SHART else FALSE
# a, b = 10, 20
# minimum = a if a < b else b
# print(minimum)
# a, b = 12, 12
# print("a = b" if a == b else "a > b" if a > b else "a < b")

# try except
try:
    n = int(input("Raqam kiriting: "))
    print(n * 2)
except ValueError:
    print("Nimadir notog'ri")
print('Hello World!')

# try:
#     n = int(input("Birinchi raqamni kiriting: "))
#     m = int(input("Ikkinchi raqamni kiriting: "))
#     print("Natija: ", n/m)
# except (ValueError, ZeroDivisionError):
#     print("Siz raqam kiritmadingiz")
#     print("Maxraj 0 bo'lishi mumkin emnas")
# else:
#     print("Xamasi yaxshi", n, 'va', m, "raqamlarini kiritdingiz")
# finally:
#     print("Program finished")

# a = input("Birinchi qiymat: ")
# b = input("Ikkinchi qiymat: ")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)