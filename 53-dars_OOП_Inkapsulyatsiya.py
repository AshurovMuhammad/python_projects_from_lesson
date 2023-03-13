# Inkapsulyatsiya // 27
# Инкапсулятсия - это закрытие каких-то данных чтобы мы могли допустим
# каким-то свойством каким-то методом получить доступ просто так изменить

# Модификаторы доступа
#   name    /   private
#   _name   /   protected
#   __name  /   private


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def set_x(self, x):  # установить
#         self.__x = x
#
#     def get_x(self):  # получить
#         return self.__x
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Kordinata raqam bo'lishi shart")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# p1 = Point(2, 50)
# # p1.set_x(100)
# # print(p1.get_x())
# # p1.set_coords(56.23, 23.8)
# print(p1.get_coords())
# # print(p1.x, p1.y)
# # p1.x = 200
# # p1.y = "hi"
# # print(p1.x, p1.y)
# print(p1.__dict__)


# import math
#
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#
#     def set_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#
#     def set_y(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def get_area(self):
#         return self.__x * self.__y
#
#     def get_per(self):
#         return 2 * (self.__x + self.__y)
#
#     def get_gip(self):
#         return math.sqrt((self.__x ** 2) + (self.__y ** 2))
#
#     def print_area(self):
#         # for i in range(self.__x):
#         #     print("*  " * self.__y)
#         print(("*  " * self.__y + '\n') * self.__x)
#
#
# p1 = Rectangle(3, 4)
# a = int(input("Bo'yi: "))
# b = int(input("Eni: "))
# p1.set_x(a)
# p1.set_y(b)
# print(p1.get_x(), p1.get_y())
# print(p1.get_area())
# print(p1.get_per())
# print(round(p1.get_gip(), 2))
# p1.print_area()
#
# p1 = Rectangle(2, 14)
# p1.print_area()


# class Point:
#     WIDTH = 5
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def set_x(self, x):  # установить
#         self.__x = x
#
#     def get_x(self):  # получить
#         return self.__x
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Kordinata raqam bo'lishi shart")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     # def __getattr__(self, item):
#     #     return f"{__class__.__name__} classda {item} atributi mavjud emas!"
#     #
#     # def __getattribute__(self, item):
#     #     if item == "_Point__x":
#     #         return "Yopiq o'zgaruvchi!"
#     #     else:
#     #         return object.__getattribute__(self, item)
#     #
#     # def __setattr__(self, key, value):
#     #     if key == "WIDTH":
#     #         raise "WIDTH qiyamtini o'zgartirib bo'lmaydi!"
#     #     else:
#     #         self.__dict__[key] = value
#
#
# p1 = Point(2, 50)
# # p1.z = 10
# # print(p1.z)
# # print(p1.zzz)
# # print(p1._Point__x)
# # print(p1.get_coords())
# # print(p1.__dict__)
# # p1.WIDTH = 7


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         if isinstance(x, (int, float)):
#             print("Setter")
#             self.__x = x
#         else:
#             raise "Nomalum ma'lumot turi!"
#
#     def __get_x(self):
#         print("Getter")
#         return self.__x
#
#     def __del_x(self):
#         print("Qiymatni o'chirish")
#         del self.__x
#
#     coordx = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coordx = 50.25     # setter
# print(p1.coordx)      # getter
# del p1.coordx         # deleter
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coordx(self):
#         print("Getter")
#         return self.__x
#
#     @coordx.setter
#     def coordx(self, x):
#         if isinstance(x, (int, float)):
#             print("Setter")
#             self.__x = x
#         else:
#             raise "Nomalum ma'lumot turi!"
#
#     @coordx.deleter
#     def coordx(self):
#         print("Qiymatni o'chirish")
#         del self.__x
#
#     # coordx = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coordx = 50.25   # setter
# print(p1.coordx)    # getter
# del p1.coordx       # deleter
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new):
#         self.__name = new
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new):
#         self.__old = new
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Anna"
# print(p1.name)
# del p1.name
# print(p1.__dict__)
# print("-"*50)
# p2 = Person("Helena", 18)
# print(p2.__dict__)
# p2.old = 20
# print(p2.old)
# del p2.old
# print(p2.__dict__)


# Heme work № 1
# class Kilogramm:
#     def __init__(self, kilo):
#         self.__kilo = kilo
#
#     @property
#     def kilo(self):
#         return self.__kilo
#
#     @kilo.setter
#     def kilo(self, new):
#         if isinstance(new, (int, float)):
#             self.__kilo = new
#         else:
#             print("Kilogramni faqat raqamlar orqali kiriting!")
#
#     def get_fnt(self):
#         res = self.__kilo * 2.205
#         return f"{self.__kilo} kg -> {res} funt"
#
#
# l1 = Kilogramm(12)
# print(l1.get_fnt())
# l1.kilo = 41
# print(l1.get_fnt())
# l1.kilo = "salom"


# Heme work № 2 // 10 ta o'zgaruvchiga getter setter deleter yozish
# class Homework:
#     def __init__(self, name, surname, age, sex, country, city, street, prof, number, car):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age
#         self.__sex = sex
#         self.__country = country
#         self.__city = city
#         self.__street = street
#         self.__prof = prof
#         self.__number = number
#         self.__car = car
#
#     # name
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new):
#         self.__name = new
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     # surname
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, new):
#         self.__surname = new
#
#     @surname.deleter
#     def surname(self):
#         del self.__surname
#
#     # age
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new):
#         self.__age = new
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#     # sex
#     @property
#     def sex(self):
#         return self.__sex
#
#     @sex.setter
#     def sex(self, new):
#         self.__sex = new
#
#     @sex.deleter
#     def sex(self):
#         del self.__sex
#
#     # country
#     @property
#     def country(self):
#         return self.__country
#
#     @country.setter
#     def country(self, new):
#         self.__country = new
#
#     @country.deleter
#     def country(self):
#         del self.__country
#
#     # city
#     @property
#     def city(self):
#         return self.__city
#
#     @city.setter
#     def city(self, new):
#         self.__city = new
#
#     @city.deleter
#     def city(self):
#         del self.__city
#
#     # street
#     @property
#     def street(self):
#         return self.__street
#
#     @street.setter
#     def street(self, new):
#         self.__street = new
#
#     @street.deleter
#     def street(self):
#         del self.__street
#
#     # profession
#     @property
#     def prof(self):
#         return self.__prof
#
#     @prof.setter
#     def prof(self, new):
#         self.__prof = new
#
#     @prof.deleter
#     def prof(self):
#         del self.__prof
#
#     # number
#     @property
#     def num(self):
#         return self.__number
#
#     @num.setter
#     def num(self, new):
#         self.__number = new
#
#     @num.deleter
#     def num(self):
#         del self.__number
#
#     # car
#     @property
#     def car(self):
#         return self.__car
#
#     @car.setter
#     def car(self, new):
#         self.__car = new
#
#     @car.deleter
#     def car(self):
#         del self.__car
#
#     def get_info(self):
#         return " Information ".center(40, "*") + f"\nName: {self.__name}\nSurname: {self.__surname}\n" \
#                f"Age: {self.__age}\nSex: {self.__sex}\nCountry: {self.__country}\n" \
#                f"City: {self.__city}\nStreet: {self.__street}\nProfession: {self.__prof}\n" \
#                f"Phone number: {self.__number}\nCar: {self.__car}\n" + "*" * 40
#
#
# p1 = Homework("Stevin", "Jobs", 25, "Man", "USA", "New-York", "Vegas", "Developer", "+998 77 777 77 77", "BMW-x5")
# p1.name = "Elon"
# print(p1.name)
# print(p1.city)
