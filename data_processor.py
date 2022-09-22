import csv
from datetime import datetime


class DataProcessor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_from_csv(self, file_path=None):
        if file_path is None:
            file_path = self.file_path

        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            reader.fieldnames = self.normalise_headers(reader.fieldnames)

            for row in reader:
                row['lease_start_date'] = datetime.strptime(row['lease_start_date'], '%d %b %Y')
                row['lease_end_date'] = datetime.strptime(row['lease_end_date'], '%d %b %Y')
                row['lease_years'] = int(row['lease_years'])
                row['current_rent'] = float(row['current_rent'])
                self.data.append(row)

    def normalise_headers(self, headers):
        return [' '.join(header.split()).replace(" ", "_").replace("[", "").replace("]", "").lower() for header in headers]

    def sort_by_current_rent(self, data=None):
        if data is None:
            data = self.data

        return sorted(data, key=lambda row: row['current_rent'])

            

        