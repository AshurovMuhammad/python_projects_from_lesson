# OOП Obyektlarga yo'naltirilgan dasturlash   // 26
# OOPda 3 ta paradima mavjud
#   1) inkapsulyatsiya
#   2) vorislik
#   3) polimorfizm


# # class <Name>:
# #     свойство(поле) = значение

# #     def __init__(self):
# #         иницализатор

# #     методы():       # функсия
# #         тело

# #     атрибут = свойство + метод


# Специальные методы:
#   Констуктор    (__new__)
#   Инитциализатор    (__init__)
#   Деструктор    (__del__)


# class Point:
#     """x, y kordinata tochkasini belgilaydi"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 120
# p1.y = 210
# print(p1.x, p1.y)
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)

# print(Point.__doc__)    # x, y kordinata tochkasini belgilaydi
# print(Point.__name__)   # Point
# print(dir(Point))


# class Point:
#     """x, y kordinata tochkasini belgilaydi"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(getattr(p1, "x"))
# print(getattr(p1, "z", "No atr"))
#
# print(hasattr(p1, 'z'))
# print(hasattr(p1, 'y'))
#
# setattr(p1, 'z', 10)
# print(p1.__dict__)
#
# delattr(p1, 'z')
# print(p1.__dict__)


# class Point:
#     x = 10
#     y = 20
#
#
# p1 = Point()
# print(type(p1))
# print(isinstance(p1, Point))


# class Point:
#     """x, y kordinata tochkasini belgilaydi"""
#     x = 1
#     y = 1
#
#     def set_name(self, name):
#         print("Hello", name)
#
#
# p1 = Point()
# p1.set_name('Mc Gregor')
# Point.set_name(p1, "Fergussion")
#
# p2 = Point()
# p2.set_name('Donic')


# class Point:
#     """x, y kordinata tochkasini belgilaydi"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coords(20, 30)
# print(p1.__dict__)


# class Human:
#     name = 'name'
#     b_day = '00.00.0000'
#     cal_num = '+998 93 197 01 97'
#     country = 'country'
#     city = 'city'
#     address = 'address'
#
#     def print_info(self):
#         print(" Shxsiy ma'lumotlar ".center(40, "*"))
#         print(f"Ism: {self.name}\nTug'ilgan sanasi: {self.b_day}\n"
#               f"Telefon raqami: {self.cal_num}\nDavlat: {self.country}\n"
#               f"Shaxar: {self.city}\nManzili: {self.address}\n" + "=" * 40)
#
#     def input_info(self, first_name, b_day, c_num, country, city, address):
#         self.name = first_name
#         self.b_day = b_day
#         self.cal_num = c_num
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Donic", "17.08.2001", "+99899 000 20 01", "Uzb", "And", "Hamkor")
# h1.print_info()
# h1.set_name("Muhammad")
# print(h1.get_name())


# class Auto:
#     model_name = ""
#     year = ""
#     brend = ""
#     horse_f = ""
#     color = ""
#     price = ""
#
#     def print_info(self):
#         print(" Avtomobil haqida ".center(40, "*"))
#         print(f"Model nomi: {self.model_name}\nChiqgan yili: {self.year}\n"
#               f"Brend: {self.brend}\nDvigatel kuchi: {self.horse_f}\n"
#               f"Rangi: {self.color}\nNarxi: {self.price}\n" + "=" * 40)
#
#     def input_info(self, model, year, brend, horse, color, price):
#         self.model_name = model
#         self.year = year
#         self.brend = brend
#         self.horse_f = horse
#         self.color = color
#         self.price = price
#
#     def get_name(self):
#         return self.model_name
#
#     def get_price(self):
#         return self.price
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# auto1 = Auto()
# auto1.input_info("Gentra", "2020", "Ravon", "1.6 dv", 'Black', '13000$')
# auto1.print_info()
# auto1.change_color('White')
# auto1.print_info()
# print(auto1.get_price())


# class Book:
#     name = ""
#     year = ""
#     genre = ""
#     author = ""
#     price = ""
#
#     def input_info(self, name, year, genre, author, price):
#         self.name = name
#         self.year = year
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def print_info(self):
#         print(" About Book ".center(40, "*"))
#         print(f"Book name: {self.name}\nWrote year: {self.year}\n"
#               f"Genre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price}\n" + "=" * 40)
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_year(self, year):
#         self.year = year
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def set_author(self, author):
#         self.author = author
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_name(self):
#         print(self.name)
#
#     def get_year(self):
#         print(self.year)
#
#     def get_genre(self):
#         print(self.genre)
#
#     def get_author(self):
#         print(self.author)
#
#     def get_price(self):
#         print(self.price)
#
#
# book1 = Book()
# book1.input_info("Sof aqida", "2022", "Muslim book", "Abdulaziz Mansur", "20 000 so'm")
# book1.print_info()
# book1.set_price("50 000 so'm")
# book1.print_info()


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Malumot: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Tajribasi", self.skill)
#
#
# p1 = Person('Muhammad', "Ashurov")
# p1.print_info()
# p1.add_skill(7)
# p2 = Person("Ali", "Valiyev")
# p2.print_info()
# p2.add_skill(15)


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("Construktor")
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Initializator")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Udaleniya ekzemplyara", self.__class__.__name__)
#
#
# p1 = Point(5, 6)
# print(p1.__dict__)


# class Point:
#     count = 0  # статическое свойство
#
#     def __init__(self, x=0, y=0):
#         self.x = x  # динамическое свойство
#         self.y = y
#         Point.count += 1
#
# p1 = Point(5, 7)
#
# p2 = Point(12, 6)
#
# print(Point.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Robots initzialization:", self.name)
#         print("Hello my name is", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "turn of")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "was last")
#         else:
#             print("Working robots:", Robot.k)
#
#
# droid1 = Robot("R-2 D-2")
# print("Counting robot:", Robot.k)
#
# droid2 = Robot("JRB")
# print("Counting robot:", Robot.k)
#
# del droid1
# del droid2
# print("Count robots:", Robot.k)
