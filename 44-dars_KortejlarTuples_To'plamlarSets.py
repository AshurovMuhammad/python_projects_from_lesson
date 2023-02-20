# kor = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(kor, id(kor))
# kor[4][0] = 'new'
# print(kor, id(kor))


# def func(lst):
#     res = []
#     for i in lst:
#         if i not in res:
#             res.append(i)
#     return tuple(reversed(res))
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))


# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)


# a = [1, 2]
# x, y = a
# print(x, y)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_maried = False
#     return name, age, is_maried
#
#
# user = get_user()
# print(user)
# x, y, z = user         # распаковка кортеж
# print(x, y, z)


# t = (1, 2, 3)
# del t
# print(t)


# tp = (1, 2, 3)
# print(tp)
# print(type(tp))
# tp = list(tp)
# print(tp)


# countries = (
#     ('Germaniya', 80.2, (('Berlin', 3.326), ('Gamburg', 1.718))),
#     ('Fransiya', 66, (('Parij', 2.2), ('Marsel', 1.6)))
# )
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nDavlat:', country_name, 'Axoli soni-', country_population)
#     for city in cities:
#         cit_name, city_population = city
#         print('\tShaxar:', cit_name, 'Axoli soni', city_population)


# set / множесва / to'plam
# a = {1, 2, 3}  # set, tuple, list, dict
# print(a)
# b = list(a)
# print(b)
# print(type(a))


# x = [i for i in range(1, 11) if i % 2 == 0]
# print(x)
# s = set(x)
# print(s)
# t = tuple(s)
# print(t)


# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 7, 7]
# num = list(set(numbers))
# print(num)


# def to_set(lst):
#     res = []
#     for i in lst:
#         res.append(i)
#     return set(res), len(lst)
#
#
# a = 'men oddiy qotorman'
# b = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(a))
# print(to_set(b))


# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# print(lst)
# st = {i for i in lst if 'a' in i}
# print(st)


# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# print(lst)
# st = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst}
# print(st)


# Shartli operator va for siqlini bir qatorda yozish /// daftarga albatta yozishim kerak
# [res for()]
# [res for() if()]
# [res if() else() for()]
# [res if() else() for() if()]


# st = {0, 1, 2, 3}
# st.add(4)
# # st.remove(1)
# # st.discard(6)
# st.pop()
# st.pop()
# print(st)


# a = {1, 2, 3}
# b = {4, 2, 1}
# # s = a.union(b)
# s = a | b
# print(s)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# un = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(un)
# print('elements:', len(un))
# print('min:', min(un))
# print('max:', max(un))


# frozenset
# a = frozenset({i for i in range(10)})
# print(a)







