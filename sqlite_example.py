# сиситема управления базами данных (СУБД) SQLite3

import sqlite3 as sq1
from sqlite3.dbapi2 import connect

path = "data/test.db"

# создание БД "text" с таблицей "text_1"

# соединение с базой данных
db = sq1.connect(path)
# обьект курсора ("Панель управления")
cursor = db.cursor()
# передача команд на языке SQL (Управление БД)
# command = """
#     create table test_1 
#     (id interger, login text, weight real)"""
# cursor.execute(command)
# # закрепление изменений
# db.commit()

# создание таблицы с проверкой на наличие
command = """
    create table if not exists test_1 
    (id interger, login text, weight real)"""
cursor.execute(command)
# закрепление изменений
db.commit()

# создание второй таблицы "text_2"
command = "CREATE TABLE IF NOT EXISTS test_2 (num INTEGER, f_name TEXT, l_name TEXT)"
cursor.execute(command)
# закрепление изменений
db.commit()


# запись в БД

# command_w = "INSERT INTO test_1 VALUES (?, ?, ?)"
# data_0 = (0, "maxim", 3.14)
# cursor.execute(command_w, data_0)

# data_1 = (1, "galya", 100.23)
# command_w = f"INSERT INTO test_1 VALUES {data_1}"
# cursor.execute(command_w)

data_2 = (1, "galya", "argunova")
command_w = f"INSERT INTO test_2 VALUES {data_2}"
cursor.execute(command_w)

data_3 = (2, "maxim", "argunova")
command_w = f"INSERT INTO test_2 VALUES {data_3}"
cursor.execute(command_w)


# db.commit()

# чтение из БД
command_1 = "SELECT * FROM test_1"
cursor.execute(command_1)
# все строки таблицы
# data = cursor.fetchall()
# # значение по одному
# print(data)
# # значение по одному
# raw_0 = cursor.fetchone()
# print(raw_0)
# raw_1 = cursor.fetchone()
# print(raw_1)
# raw_2 = cursor.fetchone()
# print(raw_2)
# raw_3 = cursor.fetchone()
# print(raw_3)
# for _ in range(5):
#     print(cursor.fetchone())

# определение кол-ва значений
print(cursor.fetchmany(2))

command_1 = "SELECT * FROM test_1"
cursor.execute(command_1)

# закрытие БД
db.close()