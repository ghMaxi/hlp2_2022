import sqlite3
from db_functions import *

PATH = 'db.sqlite'
conn = sqlite3.connect(PATH)


if db_missing_tables(conn):
    conn.close()
    from os import remove
    remove(PATH)
    conn = sqlite3.connect(PATH)
    init_db(conn)


def test():
    Category.print_table(conn)
    category1 = Category("Домашняя техника")
    category2 = Category("Стиральные машины", category1)
    category1.write_in(conn)
    category2.write_in(conn)
    Category.print_table(conn)


def product_test():
    print("--- product test ---")
    Product.print_table(conn)
    product = Product("Зубная щётка", 1)
    product.write_in(conn)
    Product.print_table(conn)


def user_test():
    print("--- user test ---")
    User.print_table(conn)
    user = User("Вася")
    user2 = User("Петя", True)
    user.write_in(conn)
    user2.write_in(conn)
    User.print_table(conn)


if __name__ == "__main__":
    test()
    # product_test()
    # user_test()
