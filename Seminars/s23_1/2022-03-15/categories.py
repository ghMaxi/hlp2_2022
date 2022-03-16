from sqlite_base import SqliteTable


class Category(SqliteTable):
    table_name = 'categories'

    @classmethod
    def make_table(cls, conn):
        query = f"""
CREATE TABLE {cls.table_name}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    parent_id INTEGER
);"""
        conn.cursor().execute(query)

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def write_to(self, conn):
        query = f"""INSERT INTO {self.table_name} (name, parent_id)
                    VALUES ('{self.name}', {self.get_parent_id(conn)})"""
        conn.cursor().execute(query)
        conn.commit()
    def get_parent_id(self, conn):
        if self.parent: return self.parent.get_id(conn)
        else: return -1
    def get_id(self, conn):
        query = f"""SELECT id FROM {self.table_name}
                    WHERE name = '{self.name}'"""
        result = conn.cursor().execute(query).fetchone()
        if result:
            return result[0]
        else:
            self.write_to(conn)
