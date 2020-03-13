import sqlite3
from export_to_db import ExportToDB
import pathlib

class PortScanExport(ExportToDB):

    def __init__(self):
        self._conn = sqlite3.connect(str(pathlib.Path(__file__).parent.absolute()) + "/PortScanRepository.db")
        self.cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def create_table(self):
        self.cursor.executescript("DROP TABLE IF EXISTS portscantabela;" 
                            "CREATE TABLE IF NOT EXISTS portscantabela"
                            "(time varchar(25), destinationport varchar(100), host varchar(100),"
                            "server varchar(100), UNIQUE(time, destinationport, host, server))")
        self._conn.commit()

    def insert_data(self, rows):
        sql = "INSERT OR IGNORE INTO portscantabela (time, destinationport, host, server) VALUES (?, ?, ?, ?);"
        self.cursor.executemany(sql, rows)
        self._conn.commit()