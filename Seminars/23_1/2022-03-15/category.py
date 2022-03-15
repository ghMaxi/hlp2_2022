class Category:
    def __init__(self, name, parent=-1):
        self.name = name
        self.parent = parent

    def insert_into(self, connection):
        query = f"""
INSERT INTO categories (name, parent)
VALUES(
    '{self.name}', '{self.parent}'
) 
"""
        connection.cursor().execute(query)
        connection.commit()
