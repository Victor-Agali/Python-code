

import pymysql

def add_favourite_to_mysql(favourite_drinks):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "BrewApp")
    cursor = connection.cursor()
    for x, y in favourite_drinks.items():
        cursor.execute(f"INSERT INTO person (name, favourite) VALUES ('{x}', '{y}')")
    connection.commit()



def load_from_sql(favourite_drinks):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "BrewApp")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM person")
    connection.commit()

    rows = cursor.fetchall()
    for row in rows:
        favourite_drinks[row[1]] = row[2]
    cursor.close()
    connection.close()