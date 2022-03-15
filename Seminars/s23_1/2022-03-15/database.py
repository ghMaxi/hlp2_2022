import sqlite3
from os import remove
from sql_scripts import init_script
PATH = 'db.sqlite'
conn = sqlite3.connect(PATH)


def db_not_okay():
    return True


def init_db():
    conn.cursor().executescript(init_script)
    conn.commit()
    query = "SELECT name FROM sqlite_master"
    print(conn.cursor().execute(query).fetchall())


if db_not_okay():
    conn.close()
    remove(PATH)
    conn = sqlite3.connect(PATH)
    init_db()
