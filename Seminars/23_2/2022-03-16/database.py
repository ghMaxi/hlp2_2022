import sqlite3


PATH = 'db.sqlite'
conn = sqlite3.connect(PATH)


def query(query_text):
    return conn.cursor().execute(query_text)


def db_is_not_okay():
    base_query = """
SELECT * FROM sqlite_master
WHERE type='table' AND name='{}'"""
    check_categories = query(base_query.format('categories')).fetchall()
    check_users = query(base_query.format('users')).fetchall()
    check_products = query(base_query.format('products')).fetchall()
    if not (check_categories and check_products and check_users):
        print("db is bad - missing tables")
        return True
    return False


def remake_db():
    global conn
    conn.close()
    from os import remove
    remove(PATH)
    conn = sqlite3.connect(PATH)

    from sql_scripts import init_script
    conn.cursor().executescript(init_script)


if db_is_not_okay():
    remake_db()


def test_add_category():
    from categories import Category
    Category.print_table(conn)
    category1 = Category("Бытовые приборы")
    category2 = Category("Тостеры", category1)
    category1.write_to(conn)
    category2.write_to(conn)
    Category.print_table(conn)


if __name__ == "__main__":
    test_add_category()
