import mysql.connector

mydb = mysql.connector.connect(
    # connects to MySQL
    host="localhost",
    user="root",
    password="Awdrgm22",
    database="usedcars"
)

my_cursor = mydb.cursor()


def create_db(name):
    my_cursor.execute("CREATE DATABASE " + name)


def create_table(name, col1):
    # VARCHAR and INTERGER declare the type of data stored in the columns with the numbers declaring their size
    my_cursor.execute(f"CREATE TABLE {name} ({col1} VARCHAR(255))")

    # saves changes!!
    mydb.commit()


def add_column(table, col, datatype, length=False):
    if length:
        my_cursor.execute(f"ALTER TABLE {table} ADD COlUMN {col} {datatype}({length})")
    else:
        my_cursor.execute(f"ALTER TABLE {table} ADD COlUMN {col} {datatype}")

def populate_table(table, *args):
    for arg in args:
        my_cursor.execute(f"INSERT INTO {table} {arg[0]} VALUES {arg[1]}")

    # saves changes!!
    mydb.commit()