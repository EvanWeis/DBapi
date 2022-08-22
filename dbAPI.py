#! usr/bin/env/python3
#python sqllite3 database api for basic CRUD functionallity

import sqlite3
from sqlite3 import Error
from config import *

def create_connection(db_file: str = ':memory:') -> None:
    '''create a database connection to SQLite database
       creates a default db in memory '''

    conn = None
    
    try: 
        
        conn = sqlite3.connect(db_file)
        print("Connection Successful...")
        print("Running Version: {}".format(sqlite3.version))
    
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(table_name: str, schema: str, drop_if: bool = True) -> None:
    '''CREATE TABLE with schema'''
    if drop_if:
        drop_table(table_name) #drop_if table exists

    try:

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("CREATE TABLE {} ({})".format(table_name, schema))
        print("Table '{}' create successfully". format(table_name))
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()

def drop_table(table_name: str) -> None:
    try:

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS {}".format(table_name))
        

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()

def insert_one(table_name: str, row: tuple) -> None:
    try:

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        for i in row:
            cur.execute("INSERT INTO {} VALUES {}".format(table_name, row))


    except Error as e:
        print(e)
    finally:
        if conn: 
            conn.commit()
            conn.close()

def insert_many(table_name: str = None, rows: list = None) -> None:
    try:

        list_len = [len(i) for i in rows]
        max_len = max(list_len)
        list_index = []
        for i in range(max_len):
            list_index.append("?")
        insert_values = ",".join(list_index)
        formatted_string = "INSERT INTO {} VALUES ({})".format(table_name, insert_values)

        conn = sqlite3.connect(db_file)
        conn.executemany(formatted_string, rows)

    except Error as e:
        print(e)
    finally:
        if conn: 
            conn.commit()
            conn.close()

def fetch_all(table_name: str) -> list:
    try: 

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM {}".format(table_name))
        return cur.fetchall()

    except Error as e:
        print(e)
    finally:
        if conn: 
            conn.close()

def fetch_one(table_name: str, cols: str, params: str = '') -> list:
    try: 

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        for row in cur.execute("SELECT {} FROM {} {}".format(cols, table_name, params)):
            return cur.fetchone()

    except Error as e:
        print(e)
    finally:
        if conn: 
            conn.close()

def update_table(table_name: str, set: str, where: str ) -> None:
    try:

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("UPDATE {} SET {} WHERE {}".format(table_name, set, where))

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()

def delete_data(table_name: str, where: str) -> None:
    try:

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('DELETE FROM {} WHERE {}'.format(table_name, where))
    
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()

def execute_query(sql_query: str) -> list: 
    try:

        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        for row in cur.execute('{}'.format(sql_query)):
            print(row)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()

def main():

    create_connection("C:\\Users\weise\Documents\\Projects\\DBAPI\\test.db")
    create_table('test', 'b text, c int')

    data = [('data', 1), ('smoke', 2), ('trust', 100), ('a', 200)]
    for i in data:
        insert_one('test ( b, c )', i )

    print('\nfetch one:')
    op = fetch_one('test', 'rowid, b,c')
    print(type(op))
    print(op)

    print("\nexecute query")
    print(execute_query('SELECT AVG(c) FROM test'))

    drop_table('test')
    create_table('test2', 'a text, b text, c text, d text, e text')

    test = [("one", "two", "three", "four", "five"),("bag", "hat","jacket", "sock", "shoe"),("apple", "pear", "grape", "orange", "banana")]

    print("\ninsert many, fetchall")
    insert_many('test2', test)

    op = fetch_all('test2')
    [print(i) for i in op]




if __name__=="__main__": main()