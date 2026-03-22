import os
from dotenv import load_dotenv
import mysql.connector

import sql_queries
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
create_db = 'FruitsAndVegetables'
table_db = 'Info'
