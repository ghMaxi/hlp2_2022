from sqlite_base import SqliteTable


class User(SqliteTable):
    table_name = 'users'

    @classmethod
    def make_table(cls, conn):
        query = f"""
CREATE TABLE {cls.table_name}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    is_seller BOOLEAN DEFAULT false
);"""
        conn.cursor().execute(query)
