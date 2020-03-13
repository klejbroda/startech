import sqlite3

class PortScanAnalyzer:

    def __init__(self):
        self._conn = sqlite3.connect("PortScanRepository.db")
        self.cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def portscan_analyzer(self):
        sql = "select count(DISTINCT(destinationport)), host, server from portscantabela"
        host_list = list(self.cursor.execute(sql))
        if host_list[0][0] >= 4:
            ip = host_list[0][1]
            query = "select time, destinationport, host, server from portscantabela where host='{}'".format(ip)
        new_list = list(self.cursor.execute(query))
        return new_list
