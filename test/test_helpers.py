import os
import sys
import unittest

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from data_processor import helpers


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.data = [
            {
                'tenant_name': 'Luke',
                'current_rent': 100.00
            },
            {
                'tenant_name': 'Leia',
                'current_rent': 50.00
            },
            {
                'tenant_name': 'Han',
                'current_rent': 200.00
            }
        ]

    def test_normalise_headers(self):
        headers = ['Property Name', 'Property  Address [2]', 'Lease Start Date']
        normalised_headers = helpers.normalise_headers(headers)
        assert normalised_headers == ['property_name', 'property_address_2', 'lease_start_date']

    def test_sort_by_key(self):
        min_rent = min(self.data, key=lambda row: row['current_rent'])['current_rent']
        max_rent = max(self.data, key=lambda row: row['current_rent'])['current_rent']

        sorted_data = helpers.sort_by_key('current_rent', self.data)
        assert sorted_data[0]['current_rent'] == min_rent
        assert sorted_data[-1]['current_rent'] == max_rent


if __name__ == '__main__':
    unittest.main()