import sqlite3
from sqlite3 import Error

# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

# import sqlite3 as sql

# con = sql.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS `test` (id INTEGER)")
#     con.commit()

# def execute_query(connection, query):
#      cursor = connection.cursor()
#      try:
#          cursor.execute(query)
#          connection.commit()
#          print("Query executed successfully")
#      except Error as e:
#          print(f"The error '{e}' occurred")

# connection = sqlite3.connect('shows.db')

# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#   id INT AUTO_INCREMENT, 
#   name TEXT NOT NULL, 
#   age INT, 
#   gender TEXT, 
#   nationality TEXT, 
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """

# create_posts_table = """
# CREATE TABLE IF NOT EXISTS posts (
#   id INT AUTO_INCREMENT, 
#   title TEXT NOT NULL, 
#   description TEXT NOT NULL, 
#   user_id INTEGER NOT NULL, 
#   FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """

# execute_query(connection, create_posts_table)

connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (Title TEXT, Director TEXT, Year INT)''')
connection.commit()
connection.close()

import sqlite3 as sql

print("1 - добавление\n2 - получение")
choice = int(input("> "))
con = sql.connect('shows.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `test` (`name` STRING, `surname` STRING)")

    if choice == 1:
        name = input("Name\n> ")
        surname = input("Surname\n> ")
        cur.execute(f"INSERT INTO `test` VALUES ('{name}', '{surname}')")
    elif choice == 2:
        cur.execute("SELECT * FROM `test`")
        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[1])
    else:
        print("Вы ошиблись")

    con.commit()
    cur.close()