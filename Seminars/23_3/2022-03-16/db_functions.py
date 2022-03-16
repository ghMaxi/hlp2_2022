from category import Category
from products import Product
from users import User


def db_missing_tables(conn):
    return True
    return (Category.not_in_db(conn) or
            Product.not_in_db(conn) or
            User.not_in_db(conn))


def init_db(conn):
    Category.make_table(conn)
    Product.make_table(conn)
    User.make_table(conn)
