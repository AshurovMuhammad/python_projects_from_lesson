# Ma'lumotlar bazasi // 45 // 71

# СУБД (система Управления Базами Данных)
# SQL - язык структурированных запросов


# Реляционная модель данных
# = = = = = =  // столбцы(ustunlar) - атрибуты, поля

# =
# =
# =         // строки(qatorlat) - обекты, кортежи, записи
# =
# =


# SQLite

# SQLiteStudio
# yoki
# DB Browser for SQLite


# Разширения - (*.db, *.db3, *.sqlite, *.sqlite3)


import sqlite3 as sq

# Tablitsa yaratish
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT, # PRIMARY KEY (PK) - birmartalik kalit, bu ma'lumotni uniqaligini taminlaydi
#     name TEXT NOT NULL,  # NOT NULL ishlatilgan qator albatta to'ldiriladi degani
#     summa REAL,
#     data TEXT
#     )
#     """)


# Yaratilgan tablitsani o'chirish
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")


# ======================================================================================================================
# SQLiteStudio editori bilan ishlash  // db_1.txt filedegi ammallar usgbu db ga moslangan

# with sq.connect("db_1.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS T1(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  # uniqal bo'lishi uchun
#     FName TEXT NOT NULL,
#     Doljnost CHAR NOT NULL,
#     ORab INTEGER,
#     ZP INTEGER
#     )
#     """)
# ======================================================================================================================

# Home Work
# db_2.txt filedegi ammallar usgbu db ga moslangan

with sq.connect("db_2.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ZAKAZ(
    CNUM INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    NAME VARCHAR (30), 
    CITY TEXT,
    RATING INTEGER,
    KOD INTEGER,
    SUM REAL,
    CITY2 TEXT,
    Prod TEXT,
    REM VARCHAR
    )
    """)
# ======================================================================================================================
