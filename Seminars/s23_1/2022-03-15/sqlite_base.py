class SqliteTable:
    table_name = 'sqlite_master'

    @classmethod
    def print_table(cls, conn):
        query = f"""SELECT * FROM {cls.table_name}"""
        result = conn.cursor().execute(query).fetchall()
        from pprint import pprint
        pprint(result)

    @classmethod
    def verify_mistakes(cls, conn):
        query = f"""SELECT * FROM sqlite_master
                    WHERE name='{cls.table_name}'"""
        if conn.cursor().execute(query).fetchall():
            print(f"{cls.table_name} found")
            return False
        print(f"{cls.table_name} not found")
        return True
