import sqlite3

try:
    sqlite_connection = sqlite3.connect('SmartHouse.db')
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    '''
    value="""INSERT INTO smart_house
          (date,temperatue,pressure,humidity)
           VALUES
           ('2021-05-26 15:22:01',16.5,123,55) """
    cursor.execute(value)
    '''
    sqlite_select_query = """SELECT * FROM smart_house"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    print("Вывод каждой строки")
    for row in records:
        print("number :", row[0])
        print("date :", row[1])
        print("temperature :", row[2])
        print("pressure :", row[3])
        print("humidity :", row[4], end="\n\n")

    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
