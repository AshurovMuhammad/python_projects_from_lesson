# Интерфейс. Связанные списки // 32 // 58


# from abc import ABC, abstractmethod
#
#
# class IFather(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(IFather):
#     def display1(self):
#         print("Child class")
#         print("Display 1 Abstract Method")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild class")
#         print("display 2 Abstract Method")
#
#
# c = GrandChild()
# c.display2()
# print()
# c.display1()


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Men tashqi class metodiman.")
#
#     def outer_object_method(self):
#         print("Men tashqi classni boglovchi metodi xisoblanaman.")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Men ichki class metodiman.")
#             MyOuter.outer_class_method()
#             print(MyOuter.age)
#             self.obj.outer_object_method()
#             print(self.obj.name)
#
#
# out = MyOuter("Tashqi")
# inner = out.MyInner("Ichki", out)
# inner.inner_method()


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee List")
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "687"
#
#         def display(self):
#             print('Name:', self.name)
#             print("Dagre:", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Albina"
#             self.id = "007"
#
#         def display(self):
#             print('Name:', self.name)
#             print("Dagre:", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
#
# d2 = outer.head
# d2.display()


# class Geeksforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is an inner class of inner class")
#
#
# outer = Geeksforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# pc = Computer()
# my_os = pc.os
# my_cpu = pc.cpu
# print(pc.name)
# print(my_os.system(), end=", ")
# print(my_cpu.make(), end=", ")
# print(my_cpu.model())
#
#
# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# pc = Computer()
# my_os = pc.OS()
# my_cpu = pc.CPU()
# print(pc.name)
# print(my_os.system(), end=", ")
# print(my_cpu.make(), end=", ")
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass().Inner()
# b.display1()
# b.display2()


# 1-usul
# class Student:
#     def __init__(self, name):
#         self.pc = self.Pc()
#         self.name = name
#
#     def show(self):
#         return self.name
#
#     class Pc:
#         def __init__(self):
#             self.model = "HP"
#             self.pr = "i7"
#             self.memory = "16"
#
#
# st = Student("Roman")
# print(st.show(), "=>", st.pc.model, st.pc.pr, st.pc.memory)
#
# st1 = Student("Alex")
# print(st1.show(), "=>", st.pc.model, st.pc.pr, st.pc.memory)


# 2-usul
# class Student:
#     def __init__(self, name):
#         self.notebook = self.Notebook()
#         self.name = name
#
#     def show(self):
#         print(self.name, end="")
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def show(self):
#             print(f" => {self.brand}, {self.cpu}, {self.ram}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
# s1.show()
# s1.notebook.show()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, "is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name, "is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name, "is braking")
#
#
# b = Dog("Buddy")
# b.bark()
# b.play()
# b.sleep()


# class A:
#     # def __init__(self):
#     #     print("Initsializator class A")
#     def hi(self):
#         print("A")
#
#
# class B(A):
#     # def __init__(self):
#     #     print("Initsializator class B")
#     def hi(self):
#         print("B")
#
#
# class C(A):
#     # def __init__(self):
#     #     print("Initsializator class C")
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     pass
#     # def __init__(self):
#         #    print("Initsializator class D")
#
#
# d = D()
# d.hi()
# print(D.mro())


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Initsializator Style class")
#         self._color = color
#         self._width = width
#
#
# class Position:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Inintsializator Position class")
#         self._sp = sp
#         self._ep = ep
#         Style.__init__(self, *args)
#
#
# class Line(Position, Style):
#     def draw(self):
#         print(f"Liniyani chizish: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


