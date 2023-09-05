import csv
class CsvWriter():
    def __init__(self, filename) -> None:
        self.filename = None
        self.header = ['title', 'content', 'link']
        self.file = open(filename, 'w')
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.header)

    def writeSingle(self, row):
        self.writer.writerow(row)
    
    def write(self, list):
        for row in list:
            self.writer.writerow(row)

    def close(self):
        self.file.close()