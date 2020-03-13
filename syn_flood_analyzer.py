import sqlite3
from collections import Counter

class SynFloodAnalyzer:

    def __init__(self):
        self._conn = sqlite3.connect("SynFloodRepository.db")
        self.cursor = self._conn.cursor()
        self.syn_requests = None
        self.ip_list = None

    def __del__(self):
        self._conn.close()

    def access_db(self):
        sql = "SELECT time, protocol, destinationport, server, flag FROM synfloodtabela WHERE protocol = 'TCP' AND flag LIKE '%syn%'"
        self.syn_requests = list(self.cursor.execute(sql))
        return self.syn_requests

    def create_ip_list(self):
        self.ip_list = []
        for element in self.syn_requests:
            self.ip_list.append(element[3])
        return self.ip_list

    def synflood_analyzer(self):
        c = Counter(self.ip_list)
        keys = list(Counter(el for el in c.elements() if c[el] >= 4).keys())
        danger = "'"+keys[0]+"'"
        sql = "SELECT time, destinationport, server, flag FROM synfloodtabela WHERE protocol = 'TCP' AND destinationport = '80' AND flag LIKE '%syn%' AND server = {}".format(danger)
        self.syn_danger = list(self.cursor.execute(sql))
        return self.syn_danger