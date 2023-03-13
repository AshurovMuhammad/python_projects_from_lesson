# Статические методы и методы класса, Наследование  // 29

# @classmethod -> Class_name.method_name()
# @staticmethod -> exemplyar.method_name() or Class_name.method_name()
# simple method -> exemplyar.method_name()


# class Account:
#     rate_usd = 0.000088
#     rate_euro = 0.000083
#     suffix = "SO'M"
#     suffix_usd = "USD"
#     suffix_euro = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname  # Egasinig familiyasi
#         self.num = num  # Xisob raqami
#         self.percent = percent  # Hisoblash foyizi
#         self.value = value  # Umumiy so'mdegi qiymati
#         print(f"№{self.num} xisobga egalik qiladi {self.surname}.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"№{self.num} {self.surname} xisobi yopildi.")
#
# #
#     @classmethod
#     def set_usd_rate(cls, rate):  # do'larga nisbatan so'm kursini o'rnatish
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):  # euroga nisbatan so'm kursini o'rnatish
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):  # Xisob egasini o'zgartirish
#         self.surname = surname
#
#     def convert_to_usd(self):  # dollarga almashtirish
#         usd_val = Account.convert(self.value, Account.rate_usd)  # local o'zgaruvchi
#         print(f"Xisob xolati: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_euro(self):  # euroga almashtirish
#         euro_val = Account.convert(self.value, Account.rate_euro)
#         print(f"Xisob xolati: {euro_val} {Account.suffix_euro}")
#
#     def add_percents(self):  # protsentni xisoblash
#         self.value += self.value * self.percent
#         print("Protsentlar muvaffaqiyatli xisoblandi!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # Kiritilgan miqdorda mablagni yechib olish
#         if val > self.value:
#             print(f"Kechirasiz sizda {val} {Account.suffix} ga yetarli mablag mavjud emas!")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} muvaffaqiyatli yechildi!")
#         self.print_balance()
#
#     def add_money(self, val): # Xisobga mablag qo'shish
#         self.value += val
#         print(f"{val} {Account.suffix} muvaffaqiyatli qo'shildi!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Mavjud balans {self.value} {Account.suffix}")
#
#     def print_info(self):  # xisob haqida ma'lumotni qaytaradi
#         print("Xisob xaqida ma'lumot")
#         print("-" * 20)
#         print(f"№{self.num}")
#         print(f"Xisob egasi: {self.surname}")
#         self.print_balance()
#         print(f"Protsentlar: {self.percent:.0%}")
#         print("-" * 20)
#
#
# ac = Account("Ashurov", 12345, 0.03, 1000)
# ac.print_info()
# ac.convert_to_usd()
# ac.convert_to_euro()
# Account.set_usd_rate(2)
# Account.set_euro_rate(5)
# print()
# ac.convert_to_usd()
# ac.convert_to_euro()
# print()
# ac.edit_owner("Helen")
# ac.print_info()
# ac.add_percents()
# ac.withdraw_money(3000)
# print()
# ac.add_money(5000)
# print()
# ac.withdraw_money(3000)


# getter,  setter,  deleter, o'zgaruvchida qo'llash
# class Account:
#     rate_usd = 0.000088
#     rate_euro = 0.000083
#     suffix = "SO'M"
#     suffix_usd = "USD"
#     suffix_euro = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__surname = surname  # Egasinig familiyasi
#         self.__num = num  # Xisob raqami
#         self.__percent = percent  # Hisoblash foyizi
#         self.__value = value  # Umumiy so'mdegi qiymati
#         print(f"№{self.__num} xisobga egalik qiladi {self.__surname}.")
#         print("*" * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):  # do'larga nisbatan so'm kursini o'rnatish
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):  # euroga nisbatan so'm kursini o'rnatish
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def __add_money(self, val):  # Xisobga mablag qo'shish
#         self.__value += val
#         print(f"{val} {Account.suffix} muvaffaqiyatli qo'shildi!")
#         print(self.print_balance())
#
#     def __print_info(self):  # xisob haqida ma'lumotni qaytaradi
#         return f"Xisob xaqida ma'lumot\n-------------------------\n" \
#                f"№{self.__num}\nXisob egasi: {self.__surname}\n" \
#                f"{self.print_balance()}\nProtsentlar: {self.__percent:.0%}\n" \
#                f"-------------------------"
#
#     def __delac(self):
#         print("*" * 50)
#         print(f"№{self.__num} {self.__surname} xisobi yopildi.")
#
#     def edit_owner(self, surname):  # Xisob egasini o'zgartirish
#         self.__surname = surname
#
#     def convert_to_usd(self):  # dollarga almashtirish
#         usd_val = Account.convert(self.__value, Account.rate_usd)  # local o'zgaruvchi
#         print(f"Xisob xolati: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_euro(self):  # euroga almashtirish
#         euro_val = Account.convert(self.__value, Account.rate_euro)
#         print(f"Xisob xolati: {euro_val} {Account.suffix_euro}")
#
#     def add_percents(self):  # protsentni xisoblash
#         self.__value += self.__value * self.__percent
#         print("Protsentlar muvaffaqiyatli xisoblandi!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # Kiritilgan miqdorda mablagni yechib olish
#         if val > self.__value:
#             print(f"Kechirasiz sizda {val} {Account.suffix} ga yetarli mablag mavjud emas!")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} muvaffaqiyatli yechildi!")
#         self.print_balance()
#
#     def print_balance(self):
#         return f"Mavjud balans {self.__value} {Account.suffix}"
#
#     account = property(__print_info, __add_money, __delac)
#
#
# ac = Account("Ashurov", 123, 0.14, 5000)
# ac.account = 7000
# print(ac.account)


# getter, setter, deleter, property methodi orqali qo'llash
# class Account:
#     rate_usd = 0.000088
#     rate_euro = 0.000083
#     suffix = "SO'M"
#     suffix_usd = "USD"
#     suffix_euro = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__surname = surname  # Egasinig familiyasi
#         self.__num = num  # Xisob raqami
#         self.__percent = percent  # Hisoblash foyizi
#         self.__value = value  # Umumiy so'mdegi qiymati
#         print(f"№{self.__num} xisobga egalik qiladi {self.__surname}.")
#         print("*" * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):  # do'larga nisbatan so'm kursini o'rnatish
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):  # euroga nisbatan so'm kursini o'rnatish
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @property
#     def account(self):  # xisob haqida ma'lumotni qaytaradi
#         return f"Xisob xaqida ma'lumot\n-------------------------\n" \
#                f"№{self.__num}\nXisob egasi: {self.__surname}\n" \
#                f"{self.print_balance()}\nProtsentlar: {self.__percent:.0%}\n" \
#                f"-------------------------"
#
#     @account.setter
#     def account(self, val):  # Xisobga mablag qo'shish
#         self.__value += val
#         print(f"{val} {Account.suffix} muvaffaqiyatli qo'shildi!")
#         print(self.print_balance())
#
#     @account.deleter
#     def account(self):
#         print("*" * 50)
#         print(f"№{self.__num} {self.__surname} xisobi yopildi.")
#
#     def edit_owner(self, surname):  # Xisob egasini o'zgartirish
#         self.__surname = surname
#
#     def convert_to_usd(self):  # dollarga almashtirish
#         usd_val = Account.convert(self.__value, Account.rate_usd)  # local o'zgaruvchi
#         print(f"Xisob xolati: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_euro(self):  # euroga almashtirish
#         euro_val = Account.convert(self.__value, Account.rate_euro)
#         print(f"Xisob xolati: {euro_val} {Account.suffix_euro}")
#
#     def add_percents(self):  # protsentni xisoblash
#         self.__value += self.__value * self.__percent
#         print("Protsentlar muvaffaqiyatli xisoblandi!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # Kiritilgan miqdorda mablagni yechib olish
#         if val > self.__value:
#             print(f"Kechirasiz sizda {val} {Account.suffix} ga yetarli mablag mavjud emas!")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} muvaffaqiyatli yechildi!")
#         self.print_balance()
#
#     def print_balance(self):
#         return f"Mavjud balans {self.__value} {Account.suffix}"
#
#
# ac = Account("Ashurov", 123, 0.14, 5000)
# ac.account = 8000
# print(ac.account)


# Наследование // Vorislik

#   Базовый класс // Родителский класс
#   Дочерний класс // Производный класс

# class Point:
#     pass
#
#
# print(isinstance(Point, object))


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Line:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw_line(self):
#         print(f"Chizilayotgan liniya: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# class Rect:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw_rect(self):
#         print(f"Chizilayotgan to'rtburchak: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(20, 25), Point(30, 44))
# rect.draw_rect()


# DRY - (Don't Repeat, Yourself)  // Takrorlamang
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Prop:  # Property - свойства
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Initsalizator Prop baza classiga tegishli")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Inintsalizator Line classiga tegishli")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Chizilayotgan liniya: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Chizilayotgan to'rtburchak: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # line.draw_line()
# # rect = Rect(Point(20, 25), Point(30, 44))
# # rect.draw_rect()
