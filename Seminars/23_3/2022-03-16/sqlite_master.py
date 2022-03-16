class SqliteMaster:
    table_name = 'sqlite_master'

    @classmethod
    def print_table(cls, conn):
        query = f"""SELECT * FROM {cls.table_name}"""
        result = conn.cursor().execute(query).fetchall()
        from pprint import pprint
        pprint(result)

    @classmethod
    def not_in_db(cls, conn):
        if cls.table_name == 'sqlite_master': return True
        result = conn.cursor().execute(f"""
SELECT * FROM sqlite_master WHERE name='{cls.table_name}'
""").fetchone()
        print(result)
        return result is None
