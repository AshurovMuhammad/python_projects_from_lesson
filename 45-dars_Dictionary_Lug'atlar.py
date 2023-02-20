# Dictionary

# d = {'one': 'bir', 'two': 'ikki'}
# print(type(d))
# print(d['one'])


# d = {'one': 'bir', 'two': 'ikki'}
# print(d)
# print(type(d))
#
# d1 = dict(one='bir', two='ikki')
# print(d1)
# print(type(d1))
#
# d2 = dict({'one': 'bir', 'two': 'ikki'})
# print(d2)
# print(type(d2))


# Dictionary lifehack
# d = dict.fromkeys(['a', 'b'], 'one')
# print(d)


# Dictionary lifehack
# users = [
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# ]
# print(users)
# d_users = dict(users)
# print(d_users)

# tp = (('a', 'b'),)
# d = dict(tp)
# print(d)


# import random
# d = {i: random.randint(20, 26) for i in range(1, 7)}
# print(d)
# print(d[5])


# d = {0: "text1", "one": 45, (1, 2, 3): 'kortej', 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[42][2])
# print('one' in d)
# del d[1, 2, 3]
# print(d)


# d = {0: "text1", "one": 45, (1, 2, 3): 'kortej', 42: [2, 3, 6, 7], True: 1}
# key = 'one1'
# try:
#     del d[key]
# except KeyError:
#     print(key, "lug'atda bunday kalit so'z mavjud emas")
# print(d)


# Dictionary lifehack
# d = {'one': 1, "two": 2, "three": 3}
# for key in d:
#     print(key, d[key])


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res = res * d[key]
# print(res)


# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("-> ")for i in range(1, 5)}
# print(d)
# ask = int(input('del num: '))
# del d[ask]
# print(d)


# Qoida!!! > Lug'atni o'chirish elementni kalit so'zi bo'yicha amalga oshadi


# d = {'one': 1, "two": 2, "three": 3}
# print(len(d))


# capitals = dict()
# capitals['Rassiya'] = 'Moskva'
# capitals['Italiya'] = 'Rim'
# capitals['Ispaniya'] = 'Madrid'
#
# countries = ['Rassiya', 'Italiya', 'Fransiya', 'Ispaniya']
#
# for country in countries:
#     if country in capitals:
#         print(country, 'davlatining poytaxti', capitals[country])
#     else:
#         print("Bazada", country, "xaqida ma'lumot yo'q")


# Dictionary yordamida maxsulotlarni sonini o'zgartirish uchun imkon beradigon dastur
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium 03220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for good in goods:
#     print(good + ')', goods[good][0], '-', str(goods[good][1]) + 'ta:', str(goods[good][2]), "so'm dan")
#
# while True:
#     ask = input('№: ')
#     if ask != '0':
#         ask2 = int(input('miqdori: '))
#         goods[ask][1] = ask2
#     else:
#         break
#
# for good in goods:
#     print(good + ')', goods[good][0], '-', str(goods[good][1]) + 'ta:', str(goods[good][2]), "so'm dan")


# Dictionary methods
# d = {"A": 1, "B": 2, "C": 3}      / Result: ['A', 'B', 'C']
# x = iter(d)
# print(x)
# print(list(x))


# d = {"A": 1, "B": 2, "C": 3}      / Result: {}
# d.clear()
# print(d)


# d = {"A": 1, "B": 2, "C": 3}      / Result: {'A': 1, 'B': 2, 'C': 3}
# d2 = d.copy()
# print(d2)


# d = {"A": 1, "B": 2, "C": 3}      / Result: 2
# value = d.get("B")
# print(value)


# d = {"A": 1, "B": 2, "C": 3}      / Result: dict_items([('A', 1), ('B', 2), ('C', 3)])
# new = d.items()
# print(new)


# d = {"A": 1, "B": 2, "C": 3}      / Result: dict_keys(['A', 'B', 'C'])
# key = d.keys()
# print(key)


# d = {"A": 1, "B": 2, "C": 3}      / Result: 2, {'A': 1, 'C': 3}
# item = d.pop('B')
# print(item)
# print(d)


# d = {"A": 1, "B": 2, "C": 3}      / Result: ('C', 3), {'A': 1, 'B': 2}
# item = d.popitem()
# print(item)
# print(d)


# d = {"A": 1, "B": 2, "C": 3}      / Result: 10, {'A': 1, 'B': 2, 'C': 3, 'E': 10}
# item = d.setdefault("E", 10)
# print(item)
# print(d)


# d = {"A": 1, "B": 2, "C": 3}      / Result: {'A': 7, 'B': 2, 'C': 3, 'Q': 9, 'F': 15}
# d.update([("A", 7), ("Q", 9), ("F", 15)])
# print(d)


# d = {"A": 1, "B": 2, "C": 3}      / Result: [1, 2, 3]
# val = d.values()
# print(list(val))


# Exercise
# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# z = dict()
# z.update(x)
# z.update(y)
# print(z)


# bio = {'name': "Muhammad", 'age': 22, 'prof': 'Developer', 'salary': 570000, 'city': 'And'}
# res = dict()
# res['name'] = bio.pop('name')
# res['salary'] = bio.pop('salary')
# print(bio)
# print(res)


# bio = {'name': "Muhammad", 'age': 22, 'prof': 'Developer', 'salary': 570000, 'city': 'And'}
# print(bio)
# bio['location'] = bio.pop('city')
# print(bio)








