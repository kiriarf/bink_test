import csv

class DataProcessor():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_from_csv(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        
        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            
            result = []

            for row in reader:
                print(row)
                result.append(row)

            return result