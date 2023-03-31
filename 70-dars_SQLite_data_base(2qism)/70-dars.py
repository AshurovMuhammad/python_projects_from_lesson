# SQLite bilan ishlash // 46 // 72

import sqlite3 as sq

with sq.connect("db_3.db") as con:
    cur = con.cursor()
    cur.execute("""
    """)

    # Bazaga ma'lumot qo'shish
    # cur.execute("""
    # INSERT INTO person
    # VALUES (10, "Olga", "79991112233", 25, "test@mail.ru")
    # """)

    # Ustunni o'chirish
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN home_address;
    # """)

    # Ustunni nomini o'zgartirish
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # """)

    # Yangi ustun qo'shish
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL DEFAULT str;
    # """)


    # Jadvalni o'chirish
    # cur.execute("""
    # DROP TABLE person_table;
    # """)

    # Jadval nomini o'zgartirish
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # Jandval yaratish
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT +998900000000,
    # age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )
    # """)




