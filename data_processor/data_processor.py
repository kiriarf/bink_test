import csv
from datetime import datetime

from . import helpers


class DataProcessor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_from_csv(self, file_path=None):
        if file_path is None:
            file_path = self.file_path

        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            reader.fieldnames = helpers.normalise_headers(reader.fieldnames)

            for row in reader:
                row['lease_start_date'] = datetime.strptime(row['lease_start_date'], '%d %b %Y')
                row['lease_end_date'] = datetime.strptime(row['lease_end_date'], '%d %b %Y')
                row['lease_years'] = int(row['lease_years'])
                row['current_rent'] = float(row['current_rent'])
                self.data.append(row)

    # def print_top_n_items_by_column(self, n=5, key='current_rent', data=None):
    #     if data is None:
    #         data = self.data



            

        