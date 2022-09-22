def normalise_headers(headers):
    """
    Takes a list of headers, and converts them to snake_case.

    :param headers: list of headers ([str])
    :returns: [str]
    """
    return [' '.join(header.split()).replace(" ", "_").replace("[", "").replace("]", "").lower() for header in headers]


def sort_by_key(key, data):
    """
    Sorts a list of dictionaries by a common key.

    :param key: by which key to sort (str)
    :param data: list of dictionaries to sort ([dict])
    :returns: [dict]
    """
    return sorted(data, key=lambda row: row[key])


def prettify_row(row):
    """
    Takes a row and returns its user-friendly representation.

    :param row: row of data (dict)
    :returns: str
    """
    address_field_values = [row['property_address_1'], row['property_address_2'], row['property_address_3'], row['property_address_4']]
    full_address = ''
    for value in address_field_values:
        if value:
            full_address += f'{value}, '

    rent_string = f'{row["current_rent"]:.2f} (from {row["lease_start_date"]:%d/%m/%Y} to {row["lease_end_date"]:%d/%m/%Y}, {row["lease_years"]} years)'

    return (f'{"Property: " + row["property_name"] + chr(10) if row["property_name"] else None}'
          f'{"Address: " + full_address[:-2] + chr(10) if full_address else None}'
          f'{"Unit: " + row["unit_name"] + chr(10) if row["unit_name"] else None}'
          f'{"Tenant: " + row["tenant_name"] + chr(10) if row["tenant_name"] else None}'
          f'{"Rent: " + rent_string if row["current_rent"] else None}')


def count_occurrences_by_key(key, data):
    """
    Returns count of each value's occurrence for a given key in a list of dictionaries.

    :param key: which key's values to count (str)
    :param data: list of dictionaries to check ([dict])
    :returns: dict
    """
    result = {}

    for row in data:
        value = row[key]
        if value in result:
            result[value] += 1
        else:
            result[value] = 1

    return result
