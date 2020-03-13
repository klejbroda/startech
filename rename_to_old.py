import glob, os

class RenameToOld:

    def rename_to_old(self):
        directory = "C:/\/Users\ipokora\Documents\Python Scripts\Final_Capstone" #tutaj będzie trzeba zmienić ścieżkę
        for filename in glob.iglob(os.path.join(directory, '*.csv')):
            os.rename(filename, filename[:-4] + '.old')