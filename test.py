import unittest
import datetime

import data_processor

CSV_PATH = 'dataset.csv'

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data_processor = data_processor.DataProcessor(CSV_PATH)


    def test_read_from_csv_reads_all_data(self):
        result = self.data_processor.read_from_csv(self.data_processor.file_path)
        assert len(result) == 42


    def test_read_from_csv_converts_types(self):
        row = self.data_processor.read_from_csv(self.data_processor.file_path)[0]
        
        lease_start_date = row['lease_start_date']
        lease_end_date = row['lease_end_date']
        assert isinstance(lease_start_date, datetime.date) and isinstance(lease_end_date, datetime.date)

        lease_years = row['lease_years']
        assert isinstance(lease_years, int)

        current_rent = row['current_rent']
        assert isinstance(current_rent, float)


    def test_normalise_headers(self):
        headers = ['Property Name', 'Property  Address [2]', 'Lease Start Date']
        normalised_headers = self.data_processor.normalise_headers(headers)
        assert normalised_headers == ['property_name', 'property_address_2', 'lease_start_date']


if __name__ == '__main__':
    unittest.main()