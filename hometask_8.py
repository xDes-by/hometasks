import sqlite3 as sql
from typing import Tuple

class Database_CRUD:
    def __init__(self, name):
        self.connect = None
        self.name = name

    def create(self):
        self.connect = sql.connect(self.name + ".db")
        cursor = self.connect.cursor()
        cursor.execute(f"""CREATE TABLE {self.name} (
                            empId INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            dept TEXT NOT NULL,
                            job_id TEXT NOT NULL,
                            salary INTEGER NOT NULL)"""
                       )
        self.connect.close()

    def read(self, ask):
        self.connect = sql.connect(self.name + ".db")
        cursor = self.connect.cursor()
        ask_return = cursor.execute(f"SELECT {ask} FROM {self.name}")
        self.connect.close()
        return ask_return

    def update(self, datas: Tuple):
        self.connect = sql.connect(self.name + ".db")
        cursor = self.connect.cursor()
        with self.connect:
            cursor.executemany(f"INSERT INTO {self.name} VALUES(?, ?, ?, ?, ?)", datas)
        self.connect.close()

    def remove(self, rm_key, rm_item):
        print(rm_key, rm_item)
        self.connect = sql.connect(self.name + ".db")
        cursor = self.connect.cursor()
        with self.connect:
            cursor.execute(f'DELETE FROM {self.name} WHERE {rm_key} = "{rm_item}"')
        self.connect.close()

d = Database_CRUD("a")

insert_table = ((1, "Jo", "IT", "ww", 2500),
       (2, "Jolo", "IT", "w8", 2300))


# d.create()
# d.read("username")
# d.update(insert_table)
# d.remove("username", "Jolo")