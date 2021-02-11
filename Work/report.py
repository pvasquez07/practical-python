#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
#
# pylint: disable=unused-variable

import sys
import tableformat
from stock import Stock
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a stock portfolio into a list of dictonaries with keys
    name, shares, price.
    """
    with open(filename) as lines:
        portdicts = parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )
        portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
        return portfolio


def read_prices(filename):
    """
    Reads in prices and outputs a dictionary mapping stock to price.
    """
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """
    Takes a list of stocks and dictionary of prices as input and returns a list of tuples
    """
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(report, formatter):
    """
    Takes in a report and outputs data in a formatted table.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

    return report


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    """
    Reads portfolio and prices files and creates and ouputs stock report
    fmt: option output report as txt, csv, html
    """
    # Read in data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create report of data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage: %s portfile pricefile fmt" % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    main(sys.argv)