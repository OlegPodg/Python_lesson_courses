import sqlite3

"""
Создать 2 таблицы в Базе Данных.
Одна будет хранить текстовые данные (1 колонка).
Другая числовые (1 колонка).
Есть список состоящий из чисел и слов.
Если элемент списка слово: записать его в соответствующую таблицу,
затем посчитать длину слова и записать ее в числовую таблицу
Если элемент списка число: проверить, если число чётное - записать его в таблицу чисел,
если нечётное, то записать во вторую таблицу слово: "нечётное".
Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
Если меньше 5, то обновить 1 запись в первой таблице на "hello"
"""

conn = sqlite3.connect("hw_bd.db")  # Create a database for numbers
cursor = conn.cursor()
# Create a table in the database for words
cursor.execute("""   
    CREATE TABLE IF NOT EXISTS 
        table_str(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            col_1 TEXT)""")
# Create a table in the database for numbers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 
        table_int(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            col_1 INTEGER)""")
# Create a list of words and numbers
list_ = ["one", "two", 3, 4, "five", 6, 7, "eight", "nine", 10, 11, "twelve"]
# Iterating over the elements of a list
for i in list_:
    if type(i) == str:  # If the list item is of type str
        # Write in word table
        cursor.execute("""INSERT INTO table_str(col_1) VALUES(?)""", (i,))
        len_i = len(i)
        cursor.execute("""INSERT INTO table_int(col_1) VALUES(?)""", (len_i,))
    elif type(i) == int:  # If the element of the list is of type int
        if i % 2 == 0:
            cursor.execute("""INSERT INTO table_int(col_1) VALUES(?)""", (i,))
        else:
            cursor.execute("""INSERT INTO table_str(col_1) VALUES("нечётное")""")

cursor.execute("""SELECT * FROM table_int""")
data = cursor.fetchall()

if len(data) > 5:  # If there are more than 5 elements in the table for numbers
    cursor.execute("""DELETE FROM table_str WHERE id=1""")
else:  # If there are less than 5 elements in the table for numbers
    cursor.execute("""UPDATE table_str SET col_1 = 'hellow'""")

cursor.execute("""SELECT * FROM table_str""")
print(cursor.fetchall())
cursor.execute("""SELECT * FROM table_int""")
print(cursor.fetchall())
