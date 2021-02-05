# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=None, delimiter=","):
    """
    Parse a CSV file into a list of records with type conversion
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If a column selctor was given, find indices of the specified columns.
        # Also narrow the set of headers used in the resulting dictionaires.
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Applirs type conversion to the row
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make dictionary or tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records