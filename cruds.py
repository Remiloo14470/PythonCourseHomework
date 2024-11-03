import sqlite3

connection = sqlite3.connect('data_base.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')


cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()


def is_included(username):
    check_users = cursor.execute("SELECT username FROM Users").fetchall()
    for user in check_users:
        if user[0] == username:
            return True
    else:
        return False


def add_products():
    check_empty = cursor.execute("SELECT * FROM Products")
    if check_empty.fetchone() is None:
        for i in range(1, 5):
            cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?,?,?,?)",
                           (f'{i}', f'Продукт{i}', f'Описание{i}', f'{i*100}'))


def get_all_products():
    cursor.execute('''SELECT * FROM Products''')
    products = cursor.fetchall()
    return products


# cursor.execute("DELETE FROM Products")
# cursor.execute("DELETE FROM Users")

initiate_db()
add_products()
get_all_products()


connection.commit()
# connection.close()