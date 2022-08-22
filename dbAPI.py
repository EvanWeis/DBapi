#! usr/bin/env/python3
#python sqllite3 database api for basic CRUD functionallity

import sqlite3
from sqlite3 import Error
from config import *

class sqlite_database:
    def __init__(self, db_name):
        self.db_file = db_name

    def create_connection(self) -> None:
        '''create a database connection to SQLite database
        creates a default db in memory '''

        self.conn = None
        
        try: 
            
            self.conn = sqlite3.connect(self.db_file)
            print("Connection Successful...")
            print("Running Version: {}".format(sqlite3.version))
        
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()


    def create_table(self, table_name: str, schema: str, drop_if: bool = True) -> None:
        '''CREATE TABLE with schema'''
        if drop_if:
            self.drop_table(table_name) #drop_if table exists

        try:

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute("CREATE TABLE {} ({})".format(table_name, schema))
            print("Table '{}' create successfully". format(table_name))
            
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.commit()
                self.conn.close()

    def drop_table(self, table_name: str) -> None:
        try:

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute("DROP TABLE IF EXISTS {}".format(table_name))
            

        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.commit()
                self.conn.close()

    def insert_one(self, table_name: str, row: tuple) -> None:
        try:

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            for i in row:
                cur.execute("INSERT INTO {} VALUES {}".format(table_name, row))


        except Error as e:
            print(e)
        finally:
            if self.conn: 
                self.conn.commit()
                self.conn.close()

    def insert_many(self, table_name: str = None, rows: list = None) -> None:
        try:

            self.list_len = [len(i) for i in rows]
            self.max_len = max(self.list_len)
            self.list_index = []
            for i in range(self.max_len):
                self.list_index.append("?")
            self.insert_values = ",".join(self.list_index)
            self.formatted_string = "INSERT INTO {} VALUES ({})".format(table_name, self.insert_values)

            self.conn = sqlite3.connect(self.db_file)
            self.conn.executemany(self.formatted_string, rows)

        except Error as e:
            print(e)
        finally:
            if self.conn: 
                self.conn.commit()
                self.conn.close()

    def fetch_all(self, table_name: str, cols: str, params: str = '') -> list:
        try: 

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute("SELECT {} FROM {} {}".format(cols, table_name, params))
            return cur.fetchall()

        except Error as e:
            print(e)
        finally:
            if self.conn: 
                self.conn.close()

    def fetch_one(self, table_name: str, cols: str, params: str = '') -> list:
        try: 

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute("SELECT {} FROM {} {}".format(cols, table_name, params))
            return cur.fetchone()

        except Error as e:
            print(e)
        finally:
            if self.conn: 
                self.conn.close()

    def update_table(self, table_name: str, set: str, where: str ) -> None:
        try:

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute("UPDATE {} SET {} WHERE {}".format(table_name, set, where))

        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.commit()
                self.conn.close()

    def delete_data(self, table_name: str, where: str) -> None:
        try:

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            cur.execute('DELETE FROM {} WHERE {}'.format(table_name, where))
        
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.commit()
                self.conn.close()

    def execute_query(self, sql_query: str) -> list: 
        try:

            self.conn = sqlite3.connect(self.db_file)
            cur = self.conn.cursor()
            for row in cur.execute('{}'.format(sql_query)):
                print(row)

        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.commit()
                self.conn.close()

def main():

    samp = sqlite_database("some.db")

    samp.create_connection()
    samp.create_table('test', 'b text, c int')

    data = [('data', 1), ('smoke', 2), ('trust', 100), ('a', 200)]
    for i in data:
        samp.insert_one('test ( b, c )', i )

    print('\nfetch one:')
    op = samp.fetch_one('test', 'rowid, b,c')
    print(op)

    print("\nexecute query")
    print(samp.execute_query('SELECT AVG(c) FROM test'))

    samp.drop_table('test')
    samp.create_table('test2', 'a text, b text, c text, d text, e text')

    test = [("one", "two", "three", "four", "five"),("bag", "hat","jacket", "sock", "shoe"),("apple", "pear", "grape", "orange", "banana")]

    print("\ninsert many, fetchall")
    samp.insert_many('test2', test)

    op = samp.fetch_all('test2', '*')
    [print(i) for i in op]

if __name__=="__main__": main()