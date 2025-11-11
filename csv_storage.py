import csv

class CSVStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, data):
        if not data:
            return
        keys = data[0].keys()
        with open(self.file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
