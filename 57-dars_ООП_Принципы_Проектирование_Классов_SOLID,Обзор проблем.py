# Принципы_Проектирование_Классов_SOLID,Обзор проблем // 31 // 66

# s = "Hello World"
# print(s.split())  # ["Hello", "World"]
# print(s.strip("dH"))

# import re
# fio = "Ashurov Muhammad Ravshanbekovich"
# letters = re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE)
# print(letters)

# s = ["hello", 'world']
# a = "".join(s[0])
# print(type(a))
# print(a)


# import re
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__passport = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("FIO matn bo'lishi kerak!")
#         f = fio.split()  # f = ["Familiya", "Ism", "Sharif"]
#         if len(f) != 3:
#             raise TypeError("FIO notog'ri formatda!")
#         letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # letters = "FamiliyaIshmSharif"
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("FIO da faqat defiz va hariflardan foydalanilsin!")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Yoshingiz raqam bo'lishi kerak 14 dan 100 gacha!")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Vazn faqat raqam bo'lishi kerek va 20 kgdan yuqori bo'lishi kerek!")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Passport ma'lumot matn ko'rinishida bo'lishi kerek!")
#         s = ps.split()
#         if len(s) != 2:
#             raise TypeError("Notog'ri formatdegi passport ma'lumotlar kiritildi!")
#         letters = "".join(re.findall(r"[A-Z]", s[0], flags=re.IGNORECASE))
#         for l in s[0]:
#             if len(l.strip(letters)) != 0 or len(s[0]) != 2:
#                 raise TypeError("Pasport seriyada xatolik!")
#         n = 7
#         if not isinstance(int(s[1]), int) or len(s[1]) != n:
#             raise TypeError("Passport raqamda xatolik!")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def passport(self):
#         return self.__passport
#
#     @passport.setter
#     def passport(self, ps):
#         self.verify_ps(ps)
#         self.__passport = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserDate("Ashurov Diyor Ravshanbekovich", 22, "AB 4561234", 70.3)
# p1.fio = "Husanov Akrom Valiyevich"
# print(p1.fio)
# p1.old = 35
# print(p1.__dict__)


# class Point:  # Yordamchi class
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:  # Asosiy (ota) class
#     def __init__(self, sp: Point, ep: Point, color: str = "Red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Koordinata raqam bo'lishi kerak!")
#
#
# class Line(Prop):  # Voris class
#     def draw_line(self):
#         print(f"Liniyani chizish: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Koordinata butun raqam bo'lishi kerak!")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Koordinata butun raqam bo'lishi kerak!")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(10, 20), Point(55, 60))
# line.draw_line()
#
# line.set_coords(Point(23, 11), Point(2, 3))
# line.draw_line()
#
# line.set_coords(Point(-10, -20))
# line.draw_line()


# Abstrac methodga misol
# class Point:  # Yordamchi class
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:  # Asosiy (ota) class
#     def __init__(self, sp: Point, ep: Point, color: str = "Red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Koordinata raqam bo'lishi kerak!")
#
#     def draw(self):   # abstractmethod
#         raise NotImplementedError("Bola class larda draw() funksiyasi bo'lishi kerek!")
#
#
# class Line(Prop):  # Voris class
#     def draw(self):
#         print(f"Liniyani chizish: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):  # Voris class
#     def draw(self):
#         print(f"To'rtburchak chizish: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):  # Voris class
#     pass
#     # def draw(self):
#     #     print(f"Ellips chizish: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figures = list()
# figures.append(Line(Point(0, 0), Point(10, 10)))
# figures.append(Line(Point(10, 10), Point(10, 20)))
# figures.append(Rect(Point(50, 50), Point(100, 100)))
# figures.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figures:
#     f.draw()


# from abc import abstractmethod, ABC
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Shaxmat figurasi chizildi!")
#
#     @abstractmethod  # abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print("Ferz e2e4 ga siljidi!")
#
#
# q = Queen()
# q.draw()
# q.move()


from abc import ABC, abstractmethod

# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_sum(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_sum = 11300
#     suffix = "USD"
#
#     def convert_to_sum(self):
#         som = self.value * Dollar.rate_to_sum
#         return som
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_sum = 12300
#     suffix = "EUR"
#
#     def convert_to_sum(self):
#         som = self.value * Euro.rate_to_sum
#         return som
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for dollar in d:
#     dollar.print_value()
#     print(f"= {dollar.convert_to_sum():.2f} SO'M")
# print("*" * 50)
# for euro in e:
#     euro.print_value()
#     print(f"= {euro.convert_to_sum():.2f} SO'M")


# import math
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("Bola class larda calc_area methodi bo'lishi kerek!")
#
#
# class SquareTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return math.pi * self._radius ** 2
#
#
# st = SquareTable(20, 10)
# st.set_sides(2)
# print(st.__dict__)
# print(st.calc_area())
#
# rt = RoundTable(radius=10)
# print(rt.__dict__)
# print(rt.calc_area())
#
# rt2 = RoundTable(radius=20)
# rt2.set_radius(60)
# print(rt2.__dict__)
# print(rt2.calc_area())
