# SQLite data base. Pycharm orqali ma'lumotlar bazaqsi bilan ishlsh49 // 75

import sqlite3 as sq

# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROm cars WHERE model LIKE "B%";
#     UPDATE cars SET price = price + 100;
#     """)
#
#     # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})
#
#     # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
#
#     # for car in cars:
#     #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#
#     # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
#     # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
#     # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
#     # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
#     # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")
#
#
# # con.commit()
# # con.close()


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# con = None
#
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
#
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Xatolik ro'y berdi")
# finally:
#     if con:
#         con.close()


# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,
#         tr_in INTEGER,
#         buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Zaparojest', 1000)")
#     last_row_id = cur.lastrowid
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Ilya', ?, ?)", (last_row_id, buy_car_id))


# Jadvaldagi ma'lumotlarni konsolga chiqarish
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#
#     for res in cur:
#         print(res['model'], res['price'])


# Ma'lumotlar bazasiga rasm joylash va undan rasmni yuklab olish // usefull
# def read_ava(n):
#     ''' ma'lmumotlar bazasiga rasm joylash uchun funksiya '''
#     try:
#         with open(f"{n}.jpg", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     ''' ma'lumotlar bazasidan rasmni yulab olish uchun funksiya '''
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     # # ma'lumotlar bazasidan birir-bir rasimni yuklab olish (func: write_ava())
#     # cur.execute("SELECT ava FROM users LIMIT 1")
#     # img = cur.fetchone()['ava']
#     # write_ava("out.png", img)
#
#     # # ma'lumotlar bazasiga rasm joylash uchun (func: read_ava())
#     # img = read_ava(1)
#     # if img:
#     #     binary = sq.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Ilya', ?, 1000)", (binary,))


# Biror-bir ma'lumotlar joylashgan ma'luotlar bazasini ichidagi barcha ma'lumotlarni bashqa bir faylga joylab so'ngra
# ushbu ma'lumotlarni yangi ma'lumotlar bazasiga joylab beradi.
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)
#
#     # # ma'lumotlar bazasini yaratishda bajarilgan barcha komandalarni sql_dump.sql fayliga yuklab beradi
#     # with open("sql_dump.sql", "w") as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     # # for sikli oqali biz cars.db faylimozni strukturasini, qanday codlar orqali tuzilgnini konsolda ko'rishimiz mumkin
#     # for sql in con.iterdump():
#     #     print(sql)


# Ma'lumotlar bazasini faylda emas kompyuterning xotirasida yaratish
# data = [('car', 'mashina'), ('hause', 'Dom'), ('tree', 'derevo'), ('color', 'svet')]
#
# con = sq.connect(":memory:")
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT
#     )
#     """)
#
#     cur.executemany("INSERT INTO dict VALUES(?, ?)", data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())

# ======================================================================================================================
# 74-dars: Freamworklar bilan tanishuv, (ORM, Shablonizator)  // 50  // 76
# WSGI (Web Server Gateway Interface) // Web server shlyuz interfeysi
# ORM (Object-Relation Mapping) // Obyekt bilan aloqador xaritalash


# Flask
# Django

# Jinja
