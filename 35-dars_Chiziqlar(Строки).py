# Chiziqlar

# print('I\'m learning Python')
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")


# name = "Muhammad"
# age = 22
# print("Mening ismim ", name, ". Meni yoshim ", age, 'da', sep='')
# print("Mening ismim " + name + ". Meni yoshim " + str(age) + 'da')
# print(f"Mening ismim {name}. Meni yoshim {age}da")


# import math as m
# print(f"PI ning qiymati {m.pi:.2f}")
# print(f"PI ning qiymati {round(m.pi, 2)}")


# a = [1, 2, 3, 4, 5, 6, 7]
# print(f"Uchinchi qiymat {a[2]}")


# name = "Ali"
# prof = 'programmist'
# lang = 'Python'
#
# message = (
#     f"Salom {name}, "
#     f"Siz {prof}siz, "
#     f"{lang} dasturlash tilida"
# )
# print(message)


# a = 73
# print(f"{{{a}}}")


# s = '''
# <div>
#     <a href="#"></a>
# </div>
# '''
# print(s)


# def square(n):
#     '''This is a function, we can get dabl n'''
#     return n**2
#
#
# print(square(5))
# print(square.__doc__)


# import math

# def cylinder(r, h):
#     """
#     Silindir hajmini hisobledi.
#
#     Silindir hajmini hisobledi berilgan radius asos yuzini kopaytirib
#     :param r: musabat raqam, asosi radiusi
#     :param h: musbat son, silindr balandligi
#     :return: musbat son, silindr hajmi
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('#'))
# print(ord('h'))
# print(ord('@'))


# ASCII kod
# stroka = 'Test string for me'
# lst = []
# for i in stroka:
#     lst.append(ord(i))
# print('ASCII kod:', lst)
#
# sum = 0
# for j in lst:
#     sum = sum + j
# lst.insert(0, round(sum/(len(lst))))
# print("O'rta arifmetigi: ", lst)
#
# lst += [x for x in [ord(x) for x in (input("-> " + " ")[:3])] if x not in lst]
# print(lst)
#
# lst.sort(reverse=True)
# print(lst)


# Tasodifiy parolni generatsiya qilish
# from random import randint
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)  # parolni tasidifiy generatsiya qilish
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res = res + random_char
#     return res
#
#
# print(random_password())
# print(random_password())


# String methods
# s = "hi, Python WORLD!"
# print(s.capitalize())   # Hello, world! i am learning python
# print(s.lower())    # hello, world! i am learning python
# print(s.upper())    # HELLO, WORLD! I AM LEARNING PYTHON
# print(s.swapcase())    # HELLO, world! i AM LEARNING pYTHON
# print(s.title())    # Hello, World! I Am Learning Python


# print(s.count("h"))    # Kiritilgan harf soni
# print(s.count("h", 1))    # 1-chi harfni tashlab ketadi
# print(s.find("Python"))    # Kiritilgan soz boshlangan indexni qaytaradi
# print(s.find("cPython"))    # -1 ni qaytaqradi
# print(s.index("Python"))    # Kiritilgan soz boshlangan indexni qaytaradi
# print(s.index("cPython"))    # ValueErrorni qaytaradi bu holatda
# print(s.rfind("l"))    # Kiritilgan qiymatini o'ng tomondan aniqlaydi
# print(s.rfind("al"))    # -1 ni qaytaradi
# print(s.rfind("l", 3, 19))


# Foydalanuvchi tomonidan kiritilgan ikki gapni o'rnini almashtirib beradi.
# ask = input("Write here: ")
# st = ask[ask.find(" ")+1:]
# fn = ask[:ask.find(" ")]
# answer = f"{st} {fn}"
# print(answer)


# Stringdegi ma'lumotlar ichidan raqamlarni ajratib oladi
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if 48 < ord(i) < 58:
#         digits += i
# print(digits)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
# print(digits)


# Qavs ichidegi ma'lumotlarni konsolga chiqaradi
# txt = "Hello (Lorem impus asd ds asd dfg) sdfsdssa"
# print(txt[txt.index('(')+1:txt.index(')')])


# stroka = 'I am learning Python. f f hello WORLD f'
# if stroka.count("f") >= 2:
#     print(stroka.find("f"), stroka.rfind("f"))
# elif stroka.count("f") == 1:
#     print(stroka.find("f"))


# Strinigni kerakli qismini ajratib olish.
# stroka = 'I am learning Python. hello WORLD'
# stroka = stroka[:stroka.find('h')] + stroka[stroka.rfind('h') + 1:]
# print(stroka)









