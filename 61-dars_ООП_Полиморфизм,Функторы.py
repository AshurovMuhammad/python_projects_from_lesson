# Полиморфизм. Функторы 35  // 57


# Home work
# abstrack metodlar - ota classni metodlarini docherniy klaslarida qo'llashga imkon beradi
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#     @abstractmethod
#     def ploshad(self):
#         pass
#
#     @abstractmethod
#     def print_figure(self):
#         pass
#
#     @abstractmethod
#     def print_info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         self.side = side
#         super().__init__(color)
#
#     def perimetr(self):
#         return 4 * self.side
#
#     def ploshad(self):
#         return self.side ** 2
#
#     def print_info(self):
#         print(
#             f"===Kvadrat===\nTomoni: {self.side}\nRangi: {self.color}\nYuzasi: {self.ploshad()}\n"
#             f"Perimetri: {self.perimetr()}")
#         self.print_figure()
#
#     def print_figure(self):
#         print(((self.side * "*") + "\n") * self.side)
#
#
# class Rect(Shape):
#     def __init__(self, side1, side2, color):
#         self.side1 = side1
#         self.side2 = side2
#         super().__init__(color)
#
#     def perimetr(self):
#         return 2 * (self.side1 + self.side2)
#
#     def ploshad(self):
#         return self.side1 * self.side2
#
#     def print_info(self):
#         print(f"===To'g'rito'rtburchak===\nTomonlari: {self.side1}, {self.side2}\n"
#               f"Rangi: {self.color}\nYuzasi: {self.ploshad()}\nPerimetri: {self.perimetr()}")
#         self.print_figure()
#
#     def print_figure(self):
#         print((("*" * self.side2) + "\n") * self.side1)
#
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3, color):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#         super().__init__(color)
#
#     def perimetr(self):
#         return self.side1 + self.side2 + self.side3
#
#     def ploshad(self):
#         return round(0.5 * self.side1 * ((self.side2 ** 2 - (0.5 * self.side1) ** 2) ** 0.5), 2)
#
#     def print_info(self):
#         print(f"===Uchburchak===\nTomonlari: {self.side1}, {self.side2}, {self.side3}\n"
#               f"Rangi: {self.color}\nPerimetri: {self.perimetr()}\nYuzasi: {self.ploshad()}")
#         self.print_figure()
#
#     def print_figure(self):
#         for i in range(self.side2):
#             print(" " * (self.side1 // 2 - i) + "*" * i + "*" + "*" * i + "\n", end="")
#
#
# f1 = Square(3, "red")
# f2 = Rect(3, 7, "green")
# f3 = Triangle(11, 6, 6, "yellow")
#
# for i in (f1, f2, f3):
#     i.print_info()


# Polimorfizm
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
#
# shape = [r1, r2, s1, s2]
# for j in shape:
#     print(j.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))  # 45
# print(t2.total(35))  # 8


# class Cat:
#     def info(self):
#         return "Men mushuk, yoshim 2da"
#
#     def make_sound(self):
#         return "Miyauuuu diyman"
#
#
# class Dog:
#     def info(self):
#         return "Men itman, yoshim 5da"
#
#     def make_sound(self):
#         return "Wowooww diyman"
#
#
# k = Cat()
# s = Dog()
# l = [k, s]
# for i in l:
#     print(i.info())
#     print(i.make_sound())


# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age}", end=' ')
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, space, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.space = space
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.space} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, spec, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}", end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, space, group, rating, topic):
#         super().__init__(last_name, first_name, age, space, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Ashurov", "Muhammaddiyor", 22, "TMJ", "15-20", 5),
#     Teacher("Zokir", "Abdullayev", 38, "TTAT", 10),
#     Graduate("Azam", "Arslonov", 25, 5, "TTAT", "M-112", "Kiber xavfsizlik")
# ]
#
# for i in group:
#     i.info()


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __str__(self):
#         return f"{self.__coords}"
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, 2, 9, -5)
# print(len(p))
# print(abs(p))
# print(p)
# # print(dir(Point))


# import math
#
#
# class Point:
#     __slots__ = ("x", "y", "length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#
# p = Point(5, 9)
# print(p.length)


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3d(Point):
#     __slots__ = "x", "y", "z"
#
#
# pt = Point3d(10, 20)
# pt.z = 30
# print(pt.__dict__)


# Functorlar
# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c = Counter()
# c()
# c()
# x = Counter()
# x()
# x()
# x()


# class yordamida
# class StripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Argument str bo'lishi kerek")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripsChars("?:!.; ")
# print(s1("  Hello world! "))

# Funksiya yordamida
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Argument str bo'lishi kerek")
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = strip_string("?:!.; ")
# print(s1("  ?Hello World! "))

