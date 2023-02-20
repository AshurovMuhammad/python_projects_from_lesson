import os.path
import time
import os.path
# print(os.path.split(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\folder3\file.txt"))
# result: ('E:\\Python+Django Lessons\\Python\\folder1\\folder2\\folder0\\folder3', 'file.txt')
# faylga yo'lni kortej xolatida qaytaradi / result: (head, tail)
#
#
# print(os.path.dirname(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\folder3\file.txt"))
# # result: E:\Python+Django Lessons\Python\folder1\folder2\folder0\folder3
# # faylgcha bo'lgan yo'lni qaytaradi
#
#
# print(os.path.basename(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\folder3\file.txt"))
# # result: file.txt
# # faylni nomini qaytaradi
#
#
# print(os.path.join(r"E:\Python+Django Lessons", "Python", "folder1", r"folder2\folder0\folder3", "file.txt"))
# result: E:\Python+Django Lessons\Python\folder1\folder2\folder0\folder3\file.txt
# # bir yoki birnechta fayilgacga bo'lgan yo'llarni birlashtirib to'liq yo'lni xosil qilib beradi


# print(os.path.exists(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\file.txt"))
# result: True
# faylgacha bo'lgan yo'lni tekshiradi agar haqiqatanham to'g'ri yo'l bo'lsa True qiymat qaytaradi aks holda False


# print(os.path.getctime(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\file.txt")) # Fayl yaratilgan vaqtni ko'rsatadi
# print(os.path.getatime(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\file.txt")) # Faylni oxirgi marta ishlatgan vaqtni ko'rsatadi
# print(os.path.getmtime(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\file.txt")) # Faylga qilinga oxirgi o'zgartirishlar vaqtni ko'rsatadi

# print(os.listdir('Work'))  # Papka ichidegi barcha fayl va papkalarni ro'yxat ko'rinishida qaytaradi  result: ['F1', 'F2', 'w.txt']
# print(os.path.getsize("one.txt"))       # Fayl razmerini qaytaradi (baytlarda)


# print(os.path.normcase(r"E:/Python+Django/Lessons/Python/folder1/Folder2"))
# result: e:\python+django\lessons\python\folder1\folder2
# yo'lni xariflarini kichkina xolatga keltiradi va sleshlarniham to'grilaydi


# print(os.path.isfile(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\file.txt"))
# result: True
# True qiymatni qaytaradi agar oxiridegi file.txt fayli haqiqatdanham mavjud bo'lsa


# print(os.path.isdir(r"E:\Python+Django Lessons\Python\folder1\folder2\folder0\file.txt"))
# result: False
# True yoki False qiymatni qaytaradi agar yo'lni oxiri papka nomi bilan tugasa


# path = r"C:\Users\HP\Downloads\pycharm-community-2021.3.1.exe"
# size = os.path.getsize(path)
# #             Kb      Mb
# kb = size // 1024 // 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
#
# print("Razmer:", kb, "Mb")
# print("Oxirgi ishlatilgan vaqti:", time.strftime("%d, %m, %Y, %H:%M:%S", time.localtime(atime)))
# print("Oxirgi o'zgartirish kiritilgan vaqti:", time.strftime("%d, %m, %Y, %H:%M:%S", time.localtime(mtime)))


# Exercise
# dirs = [r'Work\F1', r"Work\F2\F21"]
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     "Work": ['w.txt'],
#     r"Work\F1": ['f11.txt', 'f12.txt', 'f13.txt'],
#     r"Work\F2\F21": ['f211.txt', 'f212.txt']
# }
#
# for dir1, files1 in files.items():
#     for file in files1:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\\f211.txt", r"Work\F2\\f212.txt"]
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some simple text {file} file")
#
#
# def print_tre(root, topdown):
#     print(f"{root} file strukturasini {'tashidan ichiga qarab' if topdown else 'ichidan tashiga qarab'} sxemasi tuziladi")
#     for root, dirs, files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('-'*50)
#
#
# print_tre('Work', topdown=False)
# print_tre('Work', topdown=True)


# Exercise
# path = "two.txt"
# if os.path.isdir(path):
#     print(os.path.basename(path), '- dir')
# elif os.path.isfile(path):
#     print(os.path.basename(path), '- file -', os.path.getsize(path), 'bytes')
# else:
#     print('Error')


# Versiyani boshqarish tizimi // Система контроля версии // Version Control System
# GIT bilan ishlash
#   git --version // gitni versiyasini ko'rish
#   git --help // qo'shimcha malumotlar olish uchun
#   git init // yangi repazitoriya yaratish uchun buyruq
#   git status // repazitoriya statusi haqida
#   git add -A, yoki -> --all, yoki -> . // Agar -A yoki --all xolda buyrunu kiritsek, biz repazitoriyaga
#       qoyayotgan loyihamizni barcha papkasini va fayllarini gitga yuklaydi, agar fayl (example.py) nomini kiritsak
#       faqatgina o'sha fayilni yukledi
#   git commit -m "message" // git repazitoriyamizga commetn qoldirish,
#       va shu comment orqali repoyimzga yuzlanishimiz mumkin
#   .gitignore // Biz loyihamizda ko'rinishini xoxlamaydigon fayl,
#       papkalarni yashirish uchun (.gitignore) faylidan foydalanamiz
#   git commit -m "added gitignore" // Va quydegi holda commit qoldiramiz
#   git branch // Biz qaysi shox(ветка)da turganimizni qaytaradi
#   git branch branchname // Yangi shox(ветка) yaratish
#   git branch -D branchname // Shox(ветка)ni o'chirish
#   git branch readme // Readmi Shox(ветка)sini yaratib olamiz
#   git checkout branchname // Biron-bir shox(ветка)ga o'tish
#   git checkout -b new // Bu buyruq yangi shox(ветка) yaratib va unga o'tibham qoladi
#   readme.md // Ushbu faylni yaratib olamiz. (md-mark down)text
#   git commit -m "created file readme.md" // Commit yaratiladi
#   git merge readme // Bu buyruq ikki shox(ветка)ni birlashtirib beradi.
#       Bizni xolatda readme shoxdegi barcha fayillarni master fayillari bilan birlashtiradi.
#       Qoida: Yuqoridegi taktikani real holda qo'llanishni biz quydegi misolda ko'rish mumkin
#       masalan, ikki dasturchi bitta loyiha ustida ishlashsa va yakunda birlashtirib yuborgach
#       kelishilgan xolda bittasini o'chirib yuborish mumkin. Bizni xolatda readme shox(ветка)ni
#       o'chirib yuboramiz.







