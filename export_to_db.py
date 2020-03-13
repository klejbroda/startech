import sqlite3

class ExportToDB:

    def __init__(self):
        self._conn = sqlite3.connect("repository.db")
        self.cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def create_table(self):
        self.cursor.executescript("DROP TABLE IF EXISTS tabela;"
                            "CREATE TABLE IF NOT EXISTS tabela"
                            "(time varchar(25), column1 varchar(100), column2 varchar(100),"
                            "column3 varchar(100), column4 varchar(100), UNIQUE(time, column1, cloumn2, column3, column4))")
        self._conn.commit()

    def insert_data(self, rows):
        sql = "INSERT OR IGNORE INTO tabela (time, column1, cloumn2, column3, column4) VALUES (?, ?, ?, ?, ?);"
        self.cursor.executemany(sql, rows)
        self._conn.commit()



