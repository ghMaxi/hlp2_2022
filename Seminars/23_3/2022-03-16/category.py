from sqlite_master import SqliteMaster


class Category(SqliteMaster):
    table_name = 'categories'

    @staticmethod
    def make_table(conn):
        conn.cursor().execute(f"""
        CREATE TABLE {Category.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            parent_id INTEGER DEFAULT -1);""")

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def write_in(self, conn):
        query = f'''
INSERT INTO {self.table_name} (name, parent_id)
VALUES ('{self.name}', {self.get_parent_id(conn)})'''
        print(query)
        conn.cursor().execute(query)
        conn.commit()
    def get_parent_id(self, conn):
        if self.parent:
            return self.parent.get_id(conn)
        else:
            return -1

    def get_id(self, conn):
        query = f"""SELECT id FROM {self.table_name}
                    WHERE name='{self.name}'"""
        result = conn.cursor().execute(query).fetchone()
        if result:
            return result[0]
        else:
            self.write_in(conn)
            return self.get_id(conn)
