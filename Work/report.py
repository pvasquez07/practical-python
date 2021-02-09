#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
#
# pylint: disable=unused-variable

import csv
import sys
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a stock portfolio into a list of dictoaries with keys
    name, shares, price.
    """
    with open(filename) as lines:
        return parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )


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
        current_price = prices[stock["name"]]
        change = current_price - stock["price"]
        summary = (stock["name"], stock["shares"], current_price, change)
        rows.append(summary)
    return rows


def print_report(report):
    """
    Takes in a report and outputs data in a clean table
    """
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")

    return report


def portfolio_report(portfolio_filename, prices_filename):
    """
    Reads portfolio and prices files and creates and ouputs final report
    """
    # Read in data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create report of data
    report = make_report(portfolio, prices)

    # Print it out
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit("Usage: %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    main(sys.argv)