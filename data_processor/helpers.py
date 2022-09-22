def normalise_headers(headers):
    return [' '.join(header.split()).replace(" ", "_").replace("[", "").replace("]", "").lower() for header in headers]


def sort_by_key(key, data):
    return sorted(data, key=lambda row: row[key])
