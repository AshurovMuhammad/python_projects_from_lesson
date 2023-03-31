# Foreing key, Primary key. SQLite ma'lumotlar bazasi bilan ishlash (3-qism)  // 47 // 73

import sqlite3 as sq


# with sq.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     ORDER BY ID
#     """)
#
#     # Jadvaldagi ma'lumotlarni konsolga ro'yxat ko'rinishida chiqarish
#     res = cur.fetchall()
#     print(res)
#
#     # Jadvalni birinchi id raqamdagi ma'lumotni konsolga chiqarib beradi
#     res2 = cur.fetchone()
#     print(res2)
#
#     # Jadvaldagi ixtiyoriy elementlarni chiqarib beradi (poumolchaniye: birinchisidan kegingisini)
#     res3 = cur.fetchmany(2)
#     print(res3)


# Функции агрегирования
# - SUM  // Faqat raqamdan tashkil topgan ustunlar bilan ishledi
# - AVG  // Faqat raqamdan tashkil topgan ustunlar bilan ishledi
# - COUNT  // Str, Date, Int ma'lmot turi bilan ishledi
# - MIN   // Str, Date, Int ma'lmot turi bilan ishledi
# - MAX   // Str, Date, Int ma'lmot turi bilan ishledi
