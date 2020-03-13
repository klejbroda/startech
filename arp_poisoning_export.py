import sqlite3
from export_to_db import ExportToDB
import pathlib

class ArpPoisoningExport(ExportToDB):

    def __init__(self):
        self._conn = sqlite3.connect(str(pathlib.Path(__file__).parent.absolute()) + "/ArpPoisoningRepository.db")
        self.cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def create_table(self):
        self.cursor.executescript("DROP TABLE IF EXISTS arppoisoningtabela;"
                            "CREATE TABLE IF NOT EXISTS arppoisoningtabela"
                            "(time varchar(25), protocol varchar(100), sourcemac varchar(100),"
                            "flag varchar(100), UNIQUE(time, protocol, sourcemac, flag))")
        self._conn.commit()

    def insert_data(self, rows):
        sql = "INSERT OR IGNORE INTO arppoisoningtabela (time, protocol, sourcemac, flag) VALUES (?, ?, ?, ?);"
        self.cursor.executemany(sql, rows)
        self._conn.commit()
