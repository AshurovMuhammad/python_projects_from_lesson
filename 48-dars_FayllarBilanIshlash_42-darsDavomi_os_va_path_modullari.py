# f = open('text.txt', 'r+')
# print(f.write("I am learning Python!"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())

# print(f.read(3))
# print(f.tell())     # 3
# print(f.seek(1))     # 1
# print(f.read())
# print(f.tell())
# f.close()


# Tarif: width operatori manager content xisoblanadi.
# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789\ndsfsfsdfsds'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:5])


# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(ls):
#     res = map(str, ls)
#     return " ".join(res)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# with open('res_1.txt', 'r') as f:
#     for i in f:
#         print(i)
#         print(lst)
#         print(len(lst))
#
# print('Done! ')


# file_name = "res_2.txt"
# txt = 'Vodil oquv markazida python dasturlash tilini organsa boladimi ?, adsdfdlsks'
#
#
# with open(file_name, 'w') as f:
#     f.write(txt)
#
#
# def max_str(tx):
#     res = []
#     res2 = []
#     res3 = []
#     s = 0
#     for i in tx.split():
#         res.append(i)
#         res2.append(len(i))
#     res.sort(key=len)
#     co = res2.count(max(res2))
#     while co != s:
#         if max(res2) == len(res[-1]):
#             res3.append(res[-1])
#             del res[-1]
#         s += 1
#     print(res3)
#
#
# max_str(txt)


# text = "String №1\nString №2\nString №3\nString №4\nString №5\nString №6\nString №7\nString №8\n" \
#        "String №9\nString №10\n"
# with open('one.txt', 'w') as f:
#     f.write(text)


# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('String', 'Line - ')
#         fw.write(line)
#
#
# with open(write_file, 'r') as fw:
#     for i in fw:
#         print(i, end='')


# os -> operatsion sistema bilan ishlaydigon modul
# os path -> bu modul yo'llar bilan ishlaydi
import os
# print('Xozirgi ishlab turgan fayl', os.getcwd())    # Biz ishlab turgan ushbu faylni yo'lini qaytaradi

# print(os.listdir())     # Bu xolatda biz ishlayotgan papkadegi barcha fayllarni ro'yxat ko'rinishda qaytaradi

# print(os.listdir('..'))     # Bu xolatda biz ishlayotgan fayldan bitta yuqori pogonadegi barcha
                                    # fayllarni ro'yxat ko'rinishda qaytaradi

# os.mkdir("folder")      # Biz ishlayotgan papkada yangi papka yaratadi
# os.mkdir("folder1.folder2")

# os.makedirs("folder1/folder2/folder0/folder3/folder4/folder5")    # Bir nechta papkalar yaratishimiz mumkin

# os.remove('xyz.txt')       # Faylni o'chiradi

# os.rename('folder', 'test')     # Faylni yoki papkani nomini o'zgartirib beradi

# os.rename('test.txt', 'ts.txt')     # Faylni yoki papkani nomini o'zgartirib beradi,
                                        # va ichidegi qiymatlarni ham yangi fayilga joyledi

# os.rename('ts.txt', 'folder1/folder2/ts1.txt')      # Faylni yoki papkani nomini o'zgartirib uni
                                                        # boshqa bir papkaga joylaydi

# os.rename('folder1/folder2/ts1.txt', 'ts.docx')     # Faylni yoki papkani nomini o'zgartirib uni
                                                # boshqa bir papkaga turini(pdf, txt, docx ...) o'zgartirib joylaydi

# os.renames("text.txt", "text/new_text/tx.txt")      # Bu method yuqoridegi rename methodidan farqli o'laroq,
                                # o'zi papka ochib osha papkaga renames qilayotgan fayl yoki papkamizni joylab beradi

# os.rmdir('text')    # Bu method faqatgina bo'sh papkalarni o'chiradi,
                        # agar ushbu nomdegi papka yoq bo'sa yoki bo'sh bo'lmasa xato qaytaradi

# papkani qanday obyektlardan tashkil topganini ko'rsatadi,
# (topdown=True) bo'lsa tashidan ichiga qarab, (topdown=False) bo'sa ichidan tashiga qarab
# for root, dirs, files in os.walk("folder1", topdown=True):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)


# Exercise // Bosh papkalarni o'chirib beradi
# for root, dirs, files in os.walk("folder1", topdown=True):
#     if dirs == [] and files == []:
#         os.rmdir(root)
#         print(root, 'bosh papka')





