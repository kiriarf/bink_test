import unittest
import data_processor

CSV_PATH = 'dataset.csv'

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data_processor = data_processor.DataProcessor(CSV_PATH)

    def test_read_from_csv_reads_all_data(self):
        result = self.data_processor.read_from_csv(self.data_processor.file_path)
        assert len(result) == 42

if __name__ == '__main__':
    unittest.main()