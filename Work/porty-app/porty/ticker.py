# ticker.py

from .follow import follow
import csv
import sys
from . import report
from . import tableformat


def select_colums(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, names):
    rows = (row for row in rows if row["name"] in names)
    return rows


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_colums(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfile, logfile, fmt):
    """
    Creates a real-time stock ticker from a given portfolio, logfile, and table format.
    fmt: option output report as txt, csv, html
    """
    portfolio = report.read_portfolio(portfile)
    logfile = parse_stock_data(follow(logfile))
    rows = filter_symbols(logfile, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row["name"], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage: %s portfile logfile fmt" % args[0])
    ticker(args[1], args[2], args[3])


if __name__ == "__main__":
    main(sys.argv)