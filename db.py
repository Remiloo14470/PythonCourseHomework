import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
    );
    ''')


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


initiate_db()
add_products()
get_all_products()


connection.commit()
# connection.close()