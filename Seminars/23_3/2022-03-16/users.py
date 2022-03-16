from sqlite_master import SqliteMaster


class User(SqliteMaster):
    table_name = 'users'

    @staticmethod
    def make_table(conn):
        conn.cursor().execute(f"""
CREATE TABLE {User.table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    is_seller BOOLEAN DEFAULT false
);""")
