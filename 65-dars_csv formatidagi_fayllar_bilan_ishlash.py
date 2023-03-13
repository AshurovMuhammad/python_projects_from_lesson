# Паттерны проектирования. Принципы разделения паттернов на категории // 40 //63


# csv -> (comma separated values)
# csv.reader - ma'lumotlarni o'qish uchun
# csv.writer - ma'lumot yozish uchun
# csv.DictReader - class yordamida ma'lumotlarni o'qish uchun
# csv.DictWriter - class yordamida ma'lumot yozish uchun

import csv

# with open("data.csv") as f:
#     reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Fayl quyidegi ustunlarni tashkil qiladi: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Tugilgan yili {row[2]}")
#         count += 1
# print(f"Fayilda umumiy {count} qator mavjud")


# with open("data.csv") as f:
#     reader = csv.DictReader(f, delimiter=";")
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Fayl quyidegi ustunlarni tashkil qiladi: {', '.join(row)}")
#         print(f"\t{row['Ism']} - {row['Professiya']}. ", end="")
#         print(f"Tugilgan yili {row['Yili']}")
#         count += 1
# print(f"Fayilda umumiy {count} qator mavjud")


# with open("data2.csv") as f:
#     fields_name = ["Ism", "Professiya", "Yili"]
#     reader = csv.DictReader(f, fieldnames=fields_name)
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Fayl quyidegi ustunlarni tashkil qiladi: {', '.join(row)}")
#         print(f"\t{row['Ism']} - {row['Professiya']}. ", end="")
#         print(f"Tugilgan yili {row['Yili']}")
#         count += 1
#     print(f"Fayilda umumiy {count} qator mavjud")


# with open("student.csv", mode="w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Ism", "Sinf", "Yoshi"])
#     writer.writerow(["Jack", "6", "12"])
#     writer.writerow(["Mice", "7", "13"])
#     writer.writerow(["Helen", "8", "14"])
#     writer.writerow(["Tom", "9", "15"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, lineterminator="\r", delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open("sw_data.csv") as f:
#     print(f.read())


