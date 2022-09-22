from datetime import datetime
import sys

from data_processor import data_processor


def print_options():
    print('Your options are:')
    print('1. Print top N rentals by category')
    print('2. Print individual rentals and total rent with N lease years')
    print('3. Print count of masts per tenant')
    print('4. Print all rentals between two dates')
    print('5. Exit')


if __name__ == "__main__":
    file_path = sys.argv[1]
    dp = data_processor.DataProcessor(file_path)
    try:
        dp.read_from_csv(file_path)
    except FileNotFoundError:
        print('Error: File not found! Please enter a correct path to your dataset.')
        exit()

    print('Welcome to the Data Processor!\n')
    print_options()

    while True:
        option = int(input("\nSelect option (or press 6 to see options): "))

        if option == 1:
            n = input('How many items? (Press Enter for default, 5): ')
            key = input('Sort by which category? (Press Enter for default, Current Rent): ')

            if n is '':
                n = 5
            else:
                n = int(n)
            if key is '':
                key = 'current_rent'

            dp.print_top_n_items_by_column(n, key)
        elif option == 2:
            n = input('How many years? (Press Enter for default, 25): ')
            if n is '':
                n = 25
            else:
                n = int(n)

            dp.print_rows_and_total_rent_with_n_lease_years(n)
        elif option == 3:
            dp.print_count_of_masts_per_tenant()
        elif option == 4:
            print('Please enter your dates in DD/MM/YYYY format')
            start_date = input('What is the start date? (Press Enter for default, 01/06/1999): ')
            end_date = input('What is the end date? (Press Enter for default, 31/08/2007): ')

            if start_date is '':
                start_date = datetime(1999, 6, 1).date()
            else:
                start_date = datetime.strptime(start_date, '%d/%m/%Y').date()

            if end_date is '':
                end_date = datetime(2007, 8, 31).date()
            else:
                end_date = datetime.strptime(end_date, '%d/%m/%Y').date()

            dp.print_rentals_between(start_date=start_date, end_date=end_date)
        elif option == 5:
            exit()
        elif option == 6:
            print_options()
        else:
            print('Unknown option')



