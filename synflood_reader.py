from reader import LogReader
import datetime

class SynFloodReader(LogReader):

    def __init__(self):
        self.file = "synFlood.csv"

    def create_dataset(self):
        with open(self.file, "r") as self.file:
            list_of_rows = []
            contents = self.file.readlines()
            contents.pop(0)
            for row in contents:
                split_rows = row.splitlines()
                for lines in split_rows:
                    lines = lines.replace('"', '')
                    line = lines.split(',')
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    new_tuple = (current_time, line[4], line[7], line[9], line[12])
                    list_of_rows.append(new_tuple)
            return list_of_rows
