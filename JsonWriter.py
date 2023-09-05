import json

class JsonWriter():
    def __init__(self, filename) -> None:
        self.data = None
        self.filename = filename
        self.file = None
        self.writer = None

    def write(self, data):
        self.data = data
        self.filename = self.filename
        self.file = open(self.filename, 'w')
        self.writer = json.dump(data, self.file)
        self.file.close()