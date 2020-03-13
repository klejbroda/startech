import sqlite3

class ArpAnalyzer:

    def __init__(self):
        self._conn = sqlite3.connect("ArpPoisoningRepository.db")
        self.cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def arp_analyzer(self):
        sql = "select time, count(sourcemac), sourcemac from arppoisoningtabela where protocol='ARP'"
        mac_list = list(self.cursor.execute(sql))
        if mac_list[0][1] >= 2:
            foo = mac_list[0][2]
            query = "SELECT time, protocol, sourcemac, flag from arppoisoningtabela where protocol='ARP' and sourcemac = '{}'".format(foo)
            new_list = list(self.cursor.execute(query))
        return new_list