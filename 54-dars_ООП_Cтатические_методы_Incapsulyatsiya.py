# Статические методы  // 28
# OOPda obyektadan nuxsa yaratgach biz yangi svoystva yaratib olishimiz mumkin:
# example = Example(0, 0)
# example.z = 123
# print(example.z)


# class Person:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Person(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):  # if isinstance(z, int) or isinstance(z, float):
#             return True
#         else:
#             return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("No'malum ma'lumot turi!")
#
#     def __get_coords_x(self):
#         print('getter')
#         return self.__x
#
#     def __del_coords_x(self):
#         del self.__x
#
#     coordx = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coordx = 100
# print(p1.coordx)
# del p1.coordx
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
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
#
# p1 = Person("Anna", "Marie")
# p1.name = "Helen"
# print(p1.name)
# print(p1.surname)


# class KgFnt:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kilo(self):
#         return self.__kg
#
#     @kilo.setter
#     def kilo(self, new):
#         if isinstance(new, (int, float)):
#             self.__kg = new
#         else:
#             print("Error")
#
#     def result(self):
#         res = self.__kg * 2.205
#         return f"{self.__kg} kg -> {res}"
#
#
# k1 = KgFnt(12)
# k1.kilo = 42
# print(k1.result())


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(14))


# Exercise
# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         elif b > a and b > c and b > d:
#             return b
#         elif c > a and c > b and c > d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         elif b < a and b < c and b < d:
#             return b
#         elif c < a and c < b and c < d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def int_arith(a, b, c, d):
#         return (a + b + c + d)/4
#
#     @staticmethod
#     def fact(a):
#         fac = 1
#         while a >= 1:
#             fac = fac * a
#             a -= 1
#         return fac
#
#
# n1 = Numbers()
# print(n1.max(5, 6, 40, 2))
# print(n1.min(5, 6, 40, 2))
# print(n1.int_arith(1, 2, 3, 4))
# print(n1.fact(4))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     "30.12.2021",
#     "30-12-2020",
#     "01.01.2020",
#     "12.31.2020"
# ]
#
# for date in dates:
#     if Date.is_date_valid(date):
#         d = Date.from_string(date)
#         db = d.string_to_db()
#         print(db)
#     else:
#         print("Error")


# class Geom:
#     @staticmethod
#     def face(a, b, c):
#         return (a * b) / 2 * c
#
#     @staticmethod
#     def per(a, b, c):
#         return a + b + c
#
#
# print(Geom.face(4, 5, 2))
# print(Geom.per(5, 6, 7))
# d = Geom()
# print(d.per(5, 4, 3))

