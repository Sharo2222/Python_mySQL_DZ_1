import os
from dotenv import load_dotenv
import mysql.connector

from sample_queries import sql_queries
load_dotenv()
DB_USER = os.getenv("MY_SQL_USER")
DB_PASSWORD = os.getenv("MY_SQL_KEY")
DB_HOST = os.getenv("MY_SQL_HOST")
DB_PORT = os.getenv("MY_SQL_PORT")

conn = mysql.connector.connect(host = DB_HOST,
                               user = DB_USER,
                               password = DB_PASSWORD,
                               port = DB_PORT,)

conn.autocommit = True
db = 'FruitsAndVegetables'
table_db = 'Info'
columns_name = '(Id, Name, Type, Color, Calory, Comment)'
columns_data = [(1, 'Яблоко', 1, 'Красный', 120.00, 'Сладное, сочное'),
                (2, 'Апельсины', 1, 'Желтый', 150.00, 'Сочные'),
                (3,'Помидоры', 2, 'Красный', 70.00,'Сочные, на любителя'),
                (4, 'Груши ', 1, 'Желтый', 110.00, 'Довольно мгкие и сладкие'),
                (5, 'Бананы', 1, 'Желтый', 190.00, 'Сытные'),
                (6, 'Киви', 1, 'Зеленый', 200.00, 'Сладкий волосатый фрукт'),
                (7, 'Огурцы', 2, 'Зеленый', 100.00, 'Ну ...'),
                (8, 'Морковь', 2, 'Оранжевый', 140.00, 'отлично подходит к разным блюдам'),
                (9, 'Брокколи', 2, 'Белый', 90.00, 'Безвкусный, но полезный овощ'),
                (10, 'Болгарский перец', 2, 'Красный', 30.00, 'Многие говорят что сладкий, но я не верю')]

cursor = conn.cursor(buffered=True, dictionary=True)
try:
    SQL_query = sql_queries.create_db(db)
    cursor.execute(SQL_query)
except mysql.connector.Error as err:
    print("При создании Базы Данных произошла ошибка", err)
else:
    print(f'База данных {db} - успешно создана!')

try:
    SQL_query = sql_queries.create_table(table_db)
    cursor.execute(fr"USE {db};")
    cursor.execute(SQL_query)
except mysql.connector.Error as err:
    print(f'произошла ошибка при создании Таблиц в Базе {db}')
else:
    print(f'Таблицы в Базе {db} - успешно созданы')

try:
    cursor.execute(fr"USE {db};")
    for column in columns_data:
        cursor.execute(sql_queries.insert_db(table_db, columns_name, column))
except mysql.connector.Error as err:
    print(f'Ошибка при записи данных', err)
else:
    print(f'Данные в колонки успешно записанны!')

list_data = []
try:
    sql_query = sql_queries.get_data(table_db)
    cursor.execute(fr"USE {db};")
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        if row is not None:
            dict= {'Id': row['Id'], 'Name': row['Name'],
                   'Type': row['Type'], 'Color': row['Color'],
                   'Calories': row['Calory'], 'Comment': row['Comment']}
            list_data.append(dict)
        else:
            break
except mysql.connector.Error as err:
    print(err)
else:
    for data in list_data:
        print(data)
finally:
    cursor.close()



