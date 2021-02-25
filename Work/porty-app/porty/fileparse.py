#!/usr/bin/env python3
# fileparse.py
#
# Exercise 3.3

import csv
import sys
import logging

log = logging.getLogger(__name__)


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records with type conversion

    lines: Any file-like or iterable object
    select: option to specify columns as a list of strings
    types: type conversion of record (e.g.,[str, int, float])
    has_header: specify if file has header (bool)
    delimiter: specify a particular delimiter
    silence_errors: Option to not display errors (bool)
    """

    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

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
    for rowno, row in enumerate(rows, 1):
        if not row:  # Skip rows with no data
            continue

        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]

        # Applies type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make dictionary or tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records