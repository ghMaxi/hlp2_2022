import sqlite3
from category import Category
from os import remove


PATH = 'db.sqlite'
conn = sqlite3.connect(PATH)


def remake_table():
    global conn
    conn.close()
    remove(PATH)
    conn = sqlite3.connect(PATH)
    script = f"""
CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    parent INTEGER DEFAULT -1
);
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    category INTEGER NOT NULL
);
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    is_seller BOOLEAN DEFAULT false
);
"""
    conn.cursor().executescript(script)
    conn.commit()


def verify_table(name):
    query = f"SELECT name FROM sqlite_master WHERE type='table'"
    result = conn.cursor().execute(query).fetchall()
    if name in result:
        return 'ok'
    else:
        remake_table()


verify_table("categories")
verify_table("products")
verify_table("users")


def add_category(category):
    query = f"SELECT * FROM categories WHERE name='{category}'"
    if conn.cursor().execute(query).fetchall():
        print(f'category {category} already exists')
    else:
        category.insert_into(conn)


def print_request(query):
    print(conn.cursor().execute(query).fetchall())


def test():
    add_category(Category("Домашняя техника"))
    print_request("SELECT * FROM categories")


if __name__ == "__main__":
    test()
