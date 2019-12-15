import mysql.connector

mydb = mysql.connector.connect(
    # connects to MySQL
    host="",
    user="",
    password="",
    database=""
)

# my_cursor = mydb.cursor(dictionary=True)
my_cursor = mydb.cursor()


def create_db(name):
    my_cursor.execute("CREATE DATABASE " + name)


def create_table(name, col1):
    # TODO make it able to take in different date tytpes
    my_cursor.execute(f"CREATE TABLE {name} ({col1} VARCHAR(255))")
    mydb.commit()


def add_column(table, col, datatype, length=False):
    # TODO start using data type enum to save space
    if length:
        my_cursor.execute(f"ALTER TABLE {table} ADD COlUMN {col} {datatype}({length})")
    else:
        my_cursor.execute(f"ALTER TABLE {table} ADD COlUMN {col} {datatype}")


def populate_table(table, *args):
    cols = []
    vals = []
    for arg in args:
        cols.append(str(arg[0]))
        vals.append(f"'{str(arg[1])}'")
    col_string = ", ".join(cols)
    val_string = ", ".join(vals)
    sql_formula = (f"INSERT INTO {table} ({col_string}) VALUES ({val_string})")
    my_cursor.execute(sql_formula)
    mydb.commit()


def populate_table_with_dict(table, dict):
    cols = []
    vals = []
    for col, val in dict.items():
        if val:
            cols.append(col)
            vals.append(f"'{str(val)}'")
    col_string = ", ".join(cols)
    val_string = ", ".join(vals)
    sql_formula = (f"INSERT INTO {table} ({col_string}) VALUES ({val_string})")
    my_cursor.execute(sql_formula)
    mydb.commit()


def drop_col(table, col):
    my_cursor.execute(f"ALTER TABLE {table} DROP COLUMN {col}")


def update_data(table, carid, *args):
    for arg in args:
        sql_formula = (f"UPDATE {table} SET {arg[0]} = '{arg[1]}' WHERE carID = '{carid}'")
        print(sql_formula)
        my_cursor.execute(sql_formula)
        mydb.commit()


def get_row(table, col, value):
    my_cursor.execute(f"SELECT * FROM {table} WHERE {col} = '{value}'")
    data = my_cursor.fetchone()
    return data


def get_col_names(table):
    # my_cursor.execute(f"SHOW columns FROM {table}")
    data = my_cursor.execute(f"SHOW columns FROM {table}")
    return data


def get_datum(table, col, value):
    my_cursor.execute(f"SELECT {col} FROM {table} WHERE {col} = '{value}'")
    datum = my_cursor.fetchone()
    return datum[0]


def delete_entry(table, col, value):
    sql_formula = f"DELETE FROM {table} WHERE {col} = '{value}'"
    my_cursor.execute(sql_formula)
    mydb.commit()


def get_next_url():
    my_cursor.execute("SELECT url FROM urlstoscrape LIMIT 1")
    url = my_cursor.fetchone()
    if url:
        return url[0]


def delete_url(url):
    sql_formula = f"DELETE FROM urlstoscrape WHERE url = '{url}'"
    my_cursor.execute(sql_formula)
    mydb.commit()
