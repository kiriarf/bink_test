def normalise_headers(headers):
    return [' '.join(header.split()).replace(" ", "_").replace("[", "").replace("]", "").lower() for header in headers]


def sort_by_key(key, data):
    return sorted(data, key=lambda row: row[key])


def prettify_row(row):
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
    result = {}

    for row in data:
        value = row[key]
        if value in result:
            result[value] += 1
        else:
            result[value] = 1

    return result
