# Сериализатсия и десериализатсия, Строенные модули сериализатции // 38 // 62

# Упаковка данных
# Сериализатсия (кодирование) - это запись данных на диск
# Десериализатсия (декодирование) - это чтение данных

# Стандартная библиотеке Python
# marshal
# pickle
# json

# pickle methodlari:
# dump() - ma'lumotlarni faylga soxranit qiladi
# load() - fayldegi ma'lumotlarni o'qish uchun method
# dumps() - ma'lumotlarni operativ xotiraga soxranit qiladi
# loads() - ma'lumotni operativ hotiradan o'qib beradi


# import pickle


# filename = "basket.txt"
# shop_list = {
#     "Mevalar": ['Olma', "Mango"],
#     "Sabzabotlar": ["Sabzi"],
#     "Budjet": 1000
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, "rb") as fh:
#     print(pickle.load(fh))


# class Test:
#     a_number = 35
#     a_string = "salom"
#     a_list = [1, 2, 3]
#     a_tuple = (22, 33)
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#
#     def __str__(self):
#         return f"Raqam: {Test.a_number}\nString: {Test.a_string}\nRo'yxat: {Test.a_list}\n" \
#                f"Kortej: {Test.a_tuple}\nLug'at: {Test.a_dict}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f"Serializatsiya v stroku:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Deserializatsiya dannix:\n{l_obj}")


# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def red_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith("\n"):
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state["file"]
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())


# json methodlari:
# dump() - ma'lumotlarni faylga soxranit qiladi
# load() - fayldegi ma'lumotlarni o'qish uchun method
# dumps() - ma'lumotlarni operativ xotiraga soxranit qiladi
# loads() - ma'lumotni operativ hotiradan o'qib beradi


# import json
# data = {
#     "firstName": "Jane",
#     "lastName": "Djo",
#     "hobbies": ['running', 'sky diving'],
#     "age": 5,
#     "20": "one"
# }


# with open("data_file.json", "w") as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', "r") as fw:
#     print(json.load(fw))


# st = json.dumps(data, sort_keys=True)
# data = json.loads(st)
# print(data)


# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))


# import json
# from random import choice


# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(num)
#     print(tel)
#
#
# gen_person()


# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         "name": name,
#         "tel": tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#     data.append(person_dict)
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


# Home Work
# import json
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         "name": name,
#         "tel": tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons2.json"))
#     except FileNotFoundError:
#         data = {}
#     data.update(person_dict)
#     with open("persons2.json", "w") as f:
#         json.dump(data, f, indent=5)
#
#
# person2 = {}
# for i in range(5):
#     gen_person()
#     person2[i] = (gen_person())
#
# print(person2)
# write_json(person2)


# import json
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         "name": name,
#         "tel": tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open("persons3.json"))
#     except FileNotFoundError:
#         data = {}
#     data[num] = person_dict
#     with open("persons3.json", "w") as f:
#         json.dump(data, f, indent=5)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])
#
# with open("persons3.json", "r") as f:
#     print(json.load(f))

