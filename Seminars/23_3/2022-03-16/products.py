from sqlite_master import SqliteMaster


class Product(SqliteMaster):
    table_name = 'products'

    @staticmethod
    def make_table(conn):
        conn.cursor().execute(f"""
CREATE TABLE {Product.table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    store INTEGER DEFAULT 0,
    category_id INTEGER DEFAULT 1
);""")
