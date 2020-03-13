import glob

class CheckForCsv:

    def __init__(self):
        self.csv_files = None

    def check_for_csv(self):
        self.csv_files = glob.glob("C:/logs/*.csv") #ścieżka jest do zmiany
        if len(csv_files) > 0:
            return True
        else:
            return False



