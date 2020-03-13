class LogReader:

    def __init__(self):
        self.file = None

    def create_dataset(self):
        with open(self.file, "r") as self.file:
            list_of_rows = []
            contents = self.file.readlines()
            contents.pop(0)
            for row in contents:
                split_rows = row.splitlines()
                for lines in split_rows:
                    line = lines.split(",")
                    new_tuple = (line[1], line[2], line[3], line[4])
                    list_of_rows.append(new_tuple)
            return list_of_rows
