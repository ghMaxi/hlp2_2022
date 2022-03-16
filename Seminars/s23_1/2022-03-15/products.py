from sqlite_base import SqliteTable


class Product(SqliteTable):
    table_name = 'products'

    @classmethod
    def make_table(cls, conn):
        query = f"""
CREATE TABLE {cls.table_name}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    category_id INTEGER NOT NULL
);"""
        conn.cursor().execute(query)
