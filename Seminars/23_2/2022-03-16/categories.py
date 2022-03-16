class Category:
    __table_name__ = 'categories'

    @staticmethod
    def print_table(conn):
        query = f"SELECT * FROM {Category.__table_name__}"
        result = conn.cursor().execute(query).fetchall()
        from pprint import pprint
        pprint(result)

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def write_to(self, conn):
        query = f"""
INSERT INTO {self.__table_name__} (name, parent_id)
VALUES ('{self.name}', {self.get_parent_id(conn)})"""
        print(query)
        conn.cursor().execute(query)
        conn.commit()

    def get_parent_id(self, conn):
        if self.parent:
            return self.parent.get_id(conn)
        else:
            return -1

    def get_id(self, conn):
        query = f"SELECT id FROM {self.__table_name__} WHERE name='{self.name}'"
        result = conn.cursor().execute(query).fetchone()
        if result:
            return result[0]
        else:
            self.parent.write_to(conn)
            return self.parent.get_id(conn)

