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

    def print_top_n_items_by_column(self, n, key):
        if n > len(self.data):
            n = len(self.data)

        sorted_data = helpers.sort_by_key(key, self.data)

        print(f'\nTop {n} masts in ascending order (ordered by {key}):')
        for i in range(n):
            row = sorted_data[i]
            print(f'{i + 1}.')
            print(helpers.prettify_row(row))

    def print_rows_and_total_rent_with_n_lease_years(self, n):
        rows_with_n_lease_years = [row for row in self.data if row['lease_years'] == n]

        total_rent = 0

        print(f'\nAll masts with lease equal {n} years:')
        for row in rows_with_n_lease_years:
            total_rent += row['current_rent']
            print(helpers.prettify_row(row))

        print(f'\nTotal Rent: {total_rent:.2f}')

    def print_count_of_masts_per_tenant(self):
        count_dict = helpers.count_occurrences_by_key('tenant_name', self.data)
        sorted_list = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

        print('\nCount of masts for each tenant:')
        for item in sorted_list:
            if item[1] == 0:
                break
            print(f'{item[0]}: {item[1]}')

    def print_rentals_between(self, start_date, end_date):
        sorted_by_start_date = helpers.sort_by_key('lease_start_date', self.data)
        rows_to_print = [
            row for row in sorted_by_start_date
            if start_date <= row['lease_start_date'] <= end_date
        ]

        print(f'\nRentals between {start_date:%d/%m/%Y} and {end_date:%d/%m/%Y}:')
        for row in rows_to_print:
            print(helpers.prettify_row(row))





