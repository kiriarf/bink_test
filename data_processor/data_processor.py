import csv
from datetime import datetime

from . import helpers


class DataProcessor():
    """
    Class responsible for reading a dataset and printing some insights from it.
    For simplicity, I assumed that the column names are always in the format that was given.
    Otherwise, some error handling (e.g. for KeyError) could be added.

    Also, I've used some list comprehensions, but would change them to generators if working
    with larger datasets to avoid memory issues.

    :param file_path: file path of the .csv dataset (string)
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_from_csv(self, file_path=None):
        """
        Reads data from a .csv, normalises the headers to snake_case and converts
        data types of some columns

        :param file_path: file path of the .csv dataset (string | None)
        :returns: None
        """
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
        """
        Prints top n items sorted by a key from self.data.

        :param n: how many items to print (int)
        :param key: one of the keys in each item (string)
        :returns: None
        """
        # do not allow to output more rows than exist
        if n > len(self.data):
            n = len(self.data)

        sorted_data = helpers.sort_by_key(key, self.data)

        print(f'\nTop {n} masts in ascending order (ordered by {key}):')
        for i in range(n):
            row = sorted_data[i]
            print(f'{i + 1}.')
            print(helpers.prettify_row(row))

    def print_rows_and_total_rent_with_n_lease_years(self, n):
        """
        Prints all rows from self.data and total rent for those rows where lease_years is n.

        :param n: value of lease_years to find (int)
        :returns: None
        """
        rows_with_n_lease_years = [row for row in self.data if row['lease_years'] == n]

        total_rent = 0

        print(f'\nAll masts with lease equal {n} years:')
        for row in rows_with_n_lease_years:
            total_rent += row['current_rent']
            print(helpers.prettify_row(row))

        print(f'\nTotal Rent: {total_rent:.2f}')

    def print_count_of_masts_per_tenant(self):
        """
        Prints number of mast rentals for each tenant.

        :returns: None
        """
        count_dict = helpers.count_occurrences_by_key('tenant_name', self.data)
        # Sorting by number of occurences here to output in sorted order,
        # thought it was more readable.
        sorted_list = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

        print('\nCount of masts for each tenant:')
        for item in sorted_list:
            print(f'{item[0]}: {item[1]}')

    def print_rentals_between(self, start_date, end_date):
        """
        Prints all rentals, where lease_start_date is between start_date and end_date (inclusive)

        :param start_date: date from which to filter (datetime.date())
        :param end_date: date until which to filter (datetime.date())
        :returns: None
        """
        sorted_by_start_date = helpers.sort_by_key('lease_start_date', self.data)
        rows_to_print = [
            row for row in sorted_by_start_date
            if start_date <= row['lease_start_date'] <= end_date
        ]

        print(f'\nRentals between {start_date:%d/%m/%Y} and {end_date:%d/%m/%Y}:')
        for row in rows_to_print:
            print(helpers.prettify_row(row))





