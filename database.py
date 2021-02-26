import pymysql

def read_database():
    connection = pymysql.connect(
        host = "localhost",
        port = 33066,
        user = "root",
        password = "password",
        db = "BrewApp"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT person_id, name FROM person")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    read_database()


