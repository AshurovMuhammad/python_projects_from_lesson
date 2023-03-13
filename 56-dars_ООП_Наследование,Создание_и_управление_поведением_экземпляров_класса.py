# Vorislik. Class ekzemplyarlarini hulqini boshqarish  // 30 // 56

# O'zgaruvchi usuli
# setter
# getter
# deleter
#
# p = property(getter, setter, deleter)

# Dekorator usuli
# @property
# @func_name.setter
# @funk_name.deleter


# public = self.name (открытые переменные)
# protected = self._name (наследование)
# private = self.__name (закрытые переменные)


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Qiymat 0dan katta bo'lishi kerak!")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Qiymat 0dan katta bo'lishi kerak!")
#
#     def border_new(self):
#         return self.border
#
#     def area(self):
#         return self.border_new()
#         # return self.color
#         # return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "Blue", "Solid")
# print(rect.area())
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.border)


# class Liquid:  # Suyuqlik classi
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density  # suyuqlik zichligi
#
#     def edit_density(self, val):  # Zichlikni o'zgarttiradigon method
#         self._density = val
#
#     def calc_v(self, m):  # kiritilgan massaga qarab suyuqlik hajmini xisoblab beradigon funksiya
#         res = m / self._density
#         print(f"{m} kg massali {self._name}ning hajmi {res} m^3 ga teng")
#         return res
#
#     def calc_m(self, v):  # berilgan hajimga qarab suyuqlik massasini aniqlash
#         res = v * self._density
#         print(f"{v} m^3 xajimli {self._name}ning massasi {res} kg ga teng")
#         return res
#
#     def print_info(self):
#         print(f"Suyuqlik {self._name} zichligi {self._density} kg/m^3.")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)


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
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Koordinata butun raqam bo'lishi kerak!")
#
#
# line = Line(Point(10, 20), Point(55, 60))
# line.draw_line()
#
# line.set_coords(Point(23.3, 11), Point(2, 3))
# line.draw_line()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"To'trburchak:\nWidth: {self.width}\nHeight: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Backgraund: {self.fon}")
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Border: {self.border}")
#
#
# ex = RectFon(500, 400, "Grey")
# ex.show_rect()
# print()
# ex2 = RectBorder(200, 100, "1px solid blue")
# ex2.show_rect()


# class Liquid:  # Suyuqlik classi
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density  # suyuqlik zichligi
#
#     def edit_density(self, val):  # Zichlikni o'zgarttiradigon method
#         self._density = val
#
#     def calc_v(self, m):  # kiritilgan massaga qarab suyuqlik hajmini xisoblab beradigon funksiya
#         res = m / self._density
#         print(f"{m} kg massali {self._name}ning hajmi {res} m^3 ga teng")
#         return res
#
#     def calc_m(self, v):  # berilgan hajimga qarab suyuqlik massasini aniqlash
#         res = v * self._density
#         print(f"{v} m^3 xajimli {self._name}ning massasi {res} kg ga teng")
#         return res
#
#     def print_info(self):
#         print(f"Suyuqlik {self._name} zichligi {self._density} kg/m^3.")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#     def calc_v(self, m):
#         v = super().calc_v(m)
#         v_alc = m * self.strength
#         print(f"{m} kg {self._name}da {v_alc} m^3 xajimli alkogol mavjud")
#         return v, v_alc
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# 57-dars_Принципы_Проектирование_Классов_SOLID,Обзор проблем // 31 // 66
