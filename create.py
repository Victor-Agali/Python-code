
import pymysql

# def add_favourite_to_mysql():
#     connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "Other BrewApp")
#     cursor = connection.cursor()
#     cursor.execute('CREATE TABLE Favourite Drinks (name VARCHAR(500),drink VARCHAR(500), user_id INTEGER AUTO_INCREMENT PRIMARY Key)')
#     cursor.execute('SHOW TABLES')
#     # for x, y in favourite_drinks.items():
#     #     cursor.execute(f"INSERT INTO person (name, favourite) VALUES ('{x}', '{y}')")
#     connection.commit()

# add_favourite_to_mysql()


def add_favourite_to_mysql(favourite_drinks):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "MyApp")
    cursor = connection.cursor()
    for Name, Drink in favourite_drinks.items():
        cursor.execute("INSERT INTO Favourite_Drinks (Name, Drink) VALUES (%s,%s) ON DUPLICATE KEY UPDATE name = %s, drink = %s",[Name, Drink,Name, Drink])
    cursor.close()
    connection.commit()
    connection.close()

def load_from_sql(favourite_drinks):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "MyApp")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Favourite_Drinks")
    connection.commit()

    rows = cursor.fetchall()
    for row in rows:
        favourite_drinks[row[0]] = row[1]
    cursor.close()
    connection.close()