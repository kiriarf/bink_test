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
                row['lease_start_date'] = datetime.strptime(row['lease_start_date'], '%d %b %Y').date()
                row['lease_end_date'] = datetime.strptime(row['lease_end_date'], '%d %b %Y').date()
                row['lease_years'] = int(row['lease_years'])
                row['current_rent'] = float(row['current_rent'])
                self.data.append(row)

    def print_top_n_items_by_column(self, n=5, key='current_rent', data=None):
        if data is None:
            data = self.data

        if n > len(data):
            n = len(data)

        sorted_data = helpers.sort_by_key(key, data)

        print(f'Top {n} masts in ascending order (ordered by {key}):')
        for i in range(n):
            row = sorted_data[i]
            print(f'{i + 1}.')
            print(helpers.prettify_row(row))

    def print_rows_and_total_rent_with_n_lease_years(self, n=25, data=None):
        if data is None:
            data = self.data

        rows_with_n_lease_years = [row for row in data if row['lease_years'] == n]

        total_rent = 0

        print(f'All masts with lease equal {n} years:')
        for row in rows_with_n_lease_years:
            total_rent += row['current_rent']
            print(helpers.prettify_row(row))

        print(f'Total Rent: {total_rent:.2f}')

    def print_count_of_masts_per_tenant(self, data=None):
        if data is None:
            data = self.data

        count_dict = helpers.count_occurrences_by_key('tenant_name', data)
        sorted_list = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

        print('Count of masts for each tenant:')
        for item in sorted_list:
            if item[1] == 0:
                break
            print(f'{item[0]}: {item[1]}')




