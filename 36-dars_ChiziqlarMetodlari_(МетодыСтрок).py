# Chiziqlar metodlari

# stroka = 'I am learning Python. hello WORLD'
# print(stroka.startswith('I am'))
# print(stroka.endswith('WORLD'))
#
# print('abs123'.isalnum())   # string faqat raqam va harflardan iborat bo'lsa
# print('abs$123'.isalnum())
# print(''.isalnum())
#
# print("ABCabc".isalpha())   # string faqat harflardan iborat bo'lsa
# print("ABC123".isalpha())

# print("123".isdigit())      # string faqat raqamdan iborat bo'lsa
# print("123abc".isdigit())
#
# print("abc".isidentifier())     # yaroqli identifikatorlar yani (bular yordamida o'zgaruvchlarni nomlash mumkin)
# print("1abc".isidentifier())
#
# print('abc'.islower())      # stringni kichik hafirdan tashkil topganini tekshiradi
# print('Abc'.islower())
#
# print("\n \t".isspace())      # stringni ichida slashli belgilarni tekshiradi
#
# print("The Apple".istitle())
# print("ABC".isupper())
#
# print(" Ummax ".center(50, "-"))
# print("    py".lstrip())    # chapdan probellarni o'chiradi
# print("py     ".rstrip())   # o'ngdan probellarni o'chiradi
# print("https://www.python.org".lstrip("htps:/"))
# print('py.$$$;'.rstrip(";$."))
# print("https://www.python.org".lstrip("htps:/").rstrip('gro.'))
# print("    py    ".strip())
# print("https://www.python.org".strip("/org.w:pths"))


# s = "Men Nython dasturlash tilini o'rganyapman. Menga Nython dasturlash tili yoqadi"
# print(s.replace("Nython", "Python", 1))


# s = "-"
# seq = ["a", "b", "c"]
# print(s.join(seq))
#
# print("...".join(['1', '2']))
# print(':'.join("Hello"))


# print("Ivan Ivanov Ivanovich".split())
#
# print("www.python.org.ru".split(".", 1))


# a = input("-> ").split()
# print(a)


# Foydalanuvchi kiritgan ism familiyani Quydegicha chiqarib beradi (Ashurov M. R.)
# nam = input("FISh: ").split()
# print(f"{nam[0]} {nam[1][0]}. {nam[2][0]}.")

# def names():
#     nam = input("FISh ni kiriting: ").split()
#     for i in range(len(nam)):
#         if i == 0:
#             f = nam[i]
#         elif i == 1:
#             n = nam[i][0]
#         elif i == 2:
#             sh = nam[i][0]
#     print(f"{f} {n}. {sh}.")
#
#
# names()


# Ashurov Muhammad Ravshanbekovich


# ask = "Salom python dasturlash tili chat boti"
# answer = ask.split()
# print("*".join(answer))


# Регулярные выражения
import re


# s = "Men 2021 yilga mos keladigon narsani istayapmanz. Va meng albatda topaman"
# reg = 'l'
# print(re.findall(reg, s))   # stringni ichidegi biz so'ragan harifni ro'yxat ko'rinishida qayttaradi
# print(re.findall('O', s))
#
# print(re.search(reg, s))    # birinchi topgan ma'lumotini qaytaradi va qidiruvni to'xtatadi
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#
# print(re.split(reg, s))
#
# print(re.sub(reg, "!", s, 1))


# s = "Men 2021 yilga mos keladigon narsani istayapmanz. Va meng albatda topaman. 0197"
# reg = r'[0-9]'
# print(re.findall(reg, s))

# s = "Men. talabamaN."
# reg = r'[A-Za-z.]'
# print(re.findall(reg, s))

# s = "SAD d 24-asdasda dsdds sd 00 df 23. 2021-06-15T21:45. asdsd sdsd sdsd df 00 fg 59. 2021-06-15T01:09."
# reg = r'[0-2][0-3]:[0-5][0-9]'
# print(re.findall(reg, s))