import datetime
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
            },
            {
                'tenant_name': 'Luke',
                'current_rent': 300.00
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

    def test_prettify_row(self):
        row = {
            'property_name': 'Seacroft Gate (Chase) - Block 2',
            'property_address_1': 'Telecomms Apparatus',
            'property_address_2': 'Leeds',
            'property_address_3': 'Some street',
            'property_address_4': 'LS14',
            'unit_name': 'Seacroft Gate (Chase) - Block 2, WYK 0414',
            'tenant_name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
            'lease_start_date': datetime.date(2007, 8, 21),
            'lease_end_date': datetime.date(2032, 8, 20),
            'lease_years': 25,
            'current_rent': 12750.0
        }

        result = helpers.prettify_row(row)

        assert result == "Property: Seacroft Gate (Chase) - Block 2\nAddress: Telecomms Apparatus, Leeds, Some street, LS14\nUnit: Seacroft Gate (Chase) - Block 2, WYK 0414\nTenant: Hutchinson3G Uk Ltd&Everything Everywhere Ltd\nRent: 12750.00 (from 21/08/2007 to 20/08/2032, 25 years)\n"

    def test_prettify_row_with_incomplete_address(self):
        row = {
            'property_name': 'Seacroft Gate (Chase) - Block 2',
            'property_address_1': 'Telecomms Apparatus',
            'property_address_2': 'Leeds',
            'property_address_3': '',
            'property_address_4': '',
            'unit_name': 'Seacroft Gate (Chase) - Block 2, WYK 0414',
            'tenant_name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
            'lease_start_date': datetime.date(2007, 8, 21),
            'lease_end_date': datetime.date(2032, 8, 20),
            'lease_years': 25,
            'current_rent': 12750.0
        }

        result = helpers.prettify_row(row)

        assert result == "Property: Seacroft Gate (Chase) - Block 2\nAddress: Telecomms Apparatus, Leeds\nUnit: Seacroft Gate (Chase) - Block 2, WYK 0414\nTenant: Hutchinson3G Uk Ltd&Everything Everywhere Ltd\nRent: 12750.00 (from 21/08/2007 to 20/08/2032, 25 years)\n"

    def test_count_occurrences_by_key(self):
        result = helpers.count_occurrences_by_key('tenant_name', self.data)

        assert result == {
            'Luke': 2,
            'Leia': 1,
            'Han': 1
        }


if __name__ == '__main__':
    unittest.main()
