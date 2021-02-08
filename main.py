import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)# connect to existing DB or create new one
    cursor = db_connection.cursor()#get ready to read/write data
    return db_connection, cursor


def close_db(connection:sqlite3.Connection):
    connection.commit()#make sure any changes get saved
    connection.close()

def setup_db(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    banner_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gpa REAL DEFAULT 0,
    credits INTEGER DEFAULT 0
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS course(
    course_prefix TEXT NOT NULL,
    course_number INTEGER NOT NULL,
    cap INTEGER DEFAULT 20,
    description TEXT,
    PRIMARY KEY(course_prefix, course_number)
    );''')


def main():
    conn, cursor = open_db("demo_db.sqlite")
    setup_db(cursor)
    print(type(conn))
    close_db(conn)


if __name__ == '__main__':
    main()
