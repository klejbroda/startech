import sqlite3
from export_to_db import ExportToDB

class SynFloodExport(ExportToDB):

    def __init__(self):
        self._conn = sqlite3.connect("SynFloodRepository.db")
        self.cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def create_table(self):
        self.cursor.executescript("DROP TABLE IF EXISTS synfloodtabela;"
                            "CREATE TABLE IF NOT EXISTS synfloodtabela"
                            "(time varchar(25), protocol varchar(100), destinationport varchar(100),"
                            "server varchar(100), flag varchar(100), UNIQUE(time, protocol, destinationport, server, flag))")
        self._conn.commit()

    def insert_data(self, rows):
        sql = "INSERT OR IGNORE INTO synfloodtabela (time, protocol, destinationport, server, flag) VALUES (?, ?, ?, ?, ?);"
        self.cursor.executemany(sql, rows)
        self._conn.commit()