import sqlite3
from os import remove
from categories import Category
from users import User
from products import Product
from sqlite_base import SqliteTable
PATH = 'db.sqlite'
FORCE_REGEN = True
conn = sqlite3.connect(PATH)


def init_db():
    Category.make_table(conn)
    Product.make_table(conn)
    User.make_table(conn)


def db_not_okay():
    return (Category.verify_mistakes(conn) or
            Product.verify_mistakes(conn) or
            User.verify_mistakes(conn))


if FORCE_REGEN or db_not_okay():
    conn.close()
    remove(PATH)
    conn = sqlite3.connect(PATH)
    init_db()


def category_test():
    Category.print_table(conn)
    category1 = Category("Бытовые приборы")
    category2 = Category("Стиральные машины", category1)
    category1.write_to(conn)
    category2.write_to(conn)
    Category.print_table(conn)


if __name__ == "__main__":
    category_test()
