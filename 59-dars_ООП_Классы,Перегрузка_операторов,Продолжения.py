# Классы. Перегрузка операторов. Продолжения // 33 // 59

# Миксины (Mixins)/ премеси


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, "a") as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#
#
# sub = MySubClass()
# sub.display("This is a some example text for class methods. \n")


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message):
#         filename = "logfile.txt"
#         with open(filename, "a") as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message):
#         super().log(message)
#
#
# sub = MySubClass()
# sub.display("This is a some example text for class methods. \n")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixingLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"Maxsulot {self.id}: sotildi 00:00 da")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2 = NoteBook("MacBook", 2, 60200)
# n2.print_info()
# n2.save_sell_log()
# print(NoteBook.mro())


# class Clock:
#     __DAY = 86400  # 24*60*60 bir kundegi sekund
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Secundlarni butun raqam bilan kiriting!")
#
#         self.__sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.__sec % 60  # seconds
#         m = (self.__sec // 60) % 60  # minut
#         h = (self.__sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Qo'shilayotgan operantlar Clock classiga tegishli bo'lishi kerek!")
#
#         return Clock(self.__sec + other.__sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Ayrilayotgan operantlar Clock classiga tegishli bo'lishi kerek!")
#
#         return Clock(self.__sec - other.__sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Ayrilayotgan operantlar Clock classiga tegishli bo'lishi kerek!")
#
#         return Clock(self.__sec * other.__sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Ayrilayotgan operantlar Clock classiga tegishli bo'lishi kerek!")
#
#         return Clock(self.__sec // other.__sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Ayrilayotgan operantlar Clock classiga tegishli bo'lishi kerek!")
#
#         return Clock(self.__sec % other.__sec)
#
#     def __eq__(self, other):
#         return self.__sec == other.__sec
#         # if self.__sec == other.__sec:
#         #     return True
#         # return False
#
#     def __ne__(self, other):
#         return self.__sec != other.__sec
#         # return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.__sec > other.__sec
#
#     def __ge__(self, other):
#         return self.__sec >= other.__sec
#
#     def __lt__(self, other):
#         return self.__sec < other.__sec
#
#     def __le__(self, other):
#         return self.__sec <= other.__sec
#
#
# # >, >=, <, <=
#
#
# s1 = Clock(100)
# s2 = Clock(100)
# s3 = Clock(300)
# # s1 += s2 + s3
# # print(s1.get_format_time())
# # s4 = s1 - s2
# # print(s4.get_format_time())
# # s5 = s1 * s2
# # print(s5.get_format_time())
# # s6 = s1 // s2
# # print(s6.get_format_time())
# # s7 = s1 % s2
# # print(s7.get_format_time())
# if s1 == s2:
#     print("__eq__ method work. s1 == s2")
# if s2 != s3:
#     print("__ne__ method work. s2 != s3")
# if s3 > s2:
#     print("__gt__ method work. s3 > s2")
# if s3 >= s2:
#     print("__ge__ method work. s3 >= s2")
# if s2 < s3:
#     print("__lt__ method work. s2 < s3")
# if s2 <= s3:
#     print("__le__ method work. s2 <= s3")


