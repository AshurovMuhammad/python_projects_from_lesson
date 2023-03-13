# Цели и задачи модульного тестирования. Практика  // 39 // 67


# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f"Student {self.name}: {a[:-2]}"
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, student, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#         data.append({"name": student.name, "marks": student.marks})
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + '\n'
#         return f"Gruppa: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, "w") as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             tmp = {"Students": stud_list}
#             data.append(tmp["Students"])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_journal(cls, file):
#         with open(file, "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
#
# # Student.dump_to_json(st2, "student.json")
# # Student.load_from_file("student.json")
#
#
# sts = [st1, st2]
# my_group = Group(sts, "Gr Python")
# print(my_group)
# # Group.dump_group("group.json", my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
# Group.upload_journal("group.json")
#
# group22 = [st3]
# my_group2 = Group(group22, "Gr Web")
# # Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print(my_group2)
# # Group.dump_group("group.json", my_group2)
#
# # print(st1)
# # st1.add_marks(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())


# Home Work
# import json
#
#
# class Guide:
#     def __init__(self, guide_country):
#         self.guide_country = guide_country
#
#     def __str__(self):
#         return f"Ma'lumotlar: {self.guide_country}"
#
#     def add_guide(self):
#         key = input("Yangi davlatni kiriting: ")
#         value = input("Yuqoridegi davlat poytaxtini kiriting: ")
#         self.guide_country[key] = value
#         return self.guide_country
#
#     def del_guide(self):
#         key = input("O'chirib tashlamoqchi bo'lgan davlatingizni yozing: ")
#         self.guide_country.pop(key)
#         return self.guide_country
#
#     def edit_guide(self):
#         key = input("O'zgartirmoqchi bo'lgan davlatingiz nomini kiriting: ")
#         if key in self.guide_country:
#             value = input(f"{key} poytaxtini kiriting: ")
#             self.guide_country[key] = value
#         else:
#             print("Bazada bunday davlat mavjud emas!")
#             edit = input(f"Ushbu {key} davlatini poytaxti qansi?")
#             self.guide_country[key] = edit
#             print("Davlat va poytaxt bazaga qo'shildi☻!")
#
#     def search_guide(self):
#         key = input("Qaysi davlatni qidirmoqchisiz: ")
#         if key in self.guide_country:
#             print(f"{key} davlatining poytaxti {self.guide_country[key]}")
#         else:
#             print("Bazada bunday davlat mavjud emas!")
#             edit = input(f"Ushbu {key} davlatini poytaxti qansi?")
#             self.guide_country[key] = edit
#             print("Davlat va poytaxt bazaga qo'shildi☻!")
#
#     @classmethod
#     def dump_to_json(cls, guide, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         data.append(guide.guide_country)
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, file_name):
#         with open(file_name, 'r') as f:
#             print(json.load(f))
#
#
# guide = {}
#
# g = Guide(guide)
# on_off = True
# while on_off:
#     ask = input("Xozirda baza bo'sh uni to'ldiring (yes/no): ")
#     if ask == "yes":
#         g.add_guide()
#         on_off = False
#     elif ask == "no":
#         print("Bazaga malumot qo'shilmadi dastur avtoatik o'chdi!")
#         on_off = False
#     else:
#         ask = input("Xozirda baza bo'sh uni to'ldiring (yes/no): ")
#
# if len(guide) != 0:
#     while True:
#         print("\nYo'nalishni tanlang.\n"
#               "1-Bazaga ma'lumot qo'shish\n"
#               "2-Bazadan ma'lumotni o'chirish\n"
#               "3-Bazadan ma'lumotni qidirish\n"
#               "4-Ma'lumotni o'zgartirish\n"
#               "5-Malumotlarni bazaga saqlash\n"
#               "6-Bazadan ma'lumotlarni ko'rish\n"
#               "7-Ma'lumotni saqlamasdan ko'rish\n"
#               "chiqib ketish - 0\n")
#         enter = input("yo'nalishni kiriting: ")
#         if enter == '1':
#             g.add_guide()
#         elif enter == '2':
#             g.del_guide()
#         elif enter =='3':
#             g.search_guide()
#         elif enter == '4':
#             g.edit_guide()
#         elif enter == '5':
#             Guide.dump_to_json(g, "country.json")
#             Guide.load_from_file("country.json")
#         elif enter == '6':
#             Guide.load_from_file('country.json')
#         elif enter == '7':
#             print(g)
#         else:
#             print("Dastur yakullandi.")
#             break
# else:
#     print("Qayta ishga tushirish uchun (shift + F10) ni bosing!")


# import requests
# import json
#
# # request - yuborish
# # response - qabul qilish
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_completed = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("data.json", "w") as f:
#     td = list(filter(keep, todos))
#     json.dump(td, f, indent=2)
#
# with open("data.json", "r") as f:
#     print(json.load(f))
