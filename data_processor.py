import csv

class DataProcessor():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_from_csv(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        
        result = []

        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            
            reader.fieldnames = self.normalise_headers(reader.fieldnames)
            print(reader.fieldnames)
            for row in reader:
                result.append(row)

        return result

    def normalise_headers(self, headers):
        return [' '.join(header.split()).replace(" ", "_").replace("[", "").replace("]", "").lower() for header in headers]
            

        