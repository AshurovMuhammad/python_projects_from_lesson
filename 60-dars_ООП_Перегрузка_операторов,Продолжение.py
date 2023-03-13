# Перегрузка операторов. Продолжение // 34 // 60


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Notog'ri index")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Index bunut son bo'lishi kerek va manfiyham bo'lmeydi")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Buyerda butun raqam bo'lishi kerek")
#         del self.marks[key]
#
#
# s1 = Student("Sergey", [5, 5, 4, 3, 4])
# print(s1[2])
# s1[20] = 3
# print(s1.marks)
# del s1[20]
# print(s1.marks)


# class Point3D:
#     CH = "Kordinata butun raqam bo'lishi kerek!"
#     RIGHT = "Ong operant Poind3D turidan bo'lishi kerek"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
#
#     @staticmethod
#     def __check0(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             raise ZeroDivisionError("Ikkinchi operandni xech bir elementi 0 bo'lishi mumkin emas!")
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):  # print("x =", pt['x'], "x1 =", pt2['x'])
#         if not isinstance(item, str):
#             raise ValueError("Klyuch stroka bo'lishi kerak!")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("Kalitni notogri malumoti.")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Klyuch stroka bo'lishi kerak!")
#         if self.__check_value(value):
#             if key == "x":
#                 self.__x = value
#             elif key =="y":
#                 self.__y = value
#             elif key == "z":
#                 self.__z = value
#         else:
#             print("Koordinata raqam bo'lishi kerek!")
#
#
# pt = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print("Koordizata 1 stroka:", pt)
# print("Koordinata 2 stroka:", pt2)
# pt3 = pt + pt2
# print("Koordinatalar yig'indisi:", pt3)
# pt4 = pt - pt2
# print("Koordinatalar ayirmasisi:", pt4)
# pt5 = pt * pt2
# print("Koordinatalar ko'paytmasi:", pt5)
# pt6 = pt / pt2
# print("Koordinatalar bo'linmasi:", pt6)
#
# print("Kordinatalarni taqqoslash:", pt == pt2)
#
# print("x =", pt['x'], "x1 =", pt2['x'])
# print("y =", pt['y'], "y1 =", pt2['y'])
# print("z =", pt['z'], "z1 =", pt2['z'])
#
# pt["x"] = 20
# print("x koordinatasiga yozilgan qiymat:", pt["x"])






