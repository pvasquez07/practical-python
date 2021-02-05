# report.py
#
# Exercise 2.4
#
# pylint: disable=unused-variable

import csv


def read_portfolio(filename):
    """
    Opens a given portfolio file and reads it into a list of tuples
    """
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            holding = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    """
    Reads in prices and outputs a dictionary of stock:price
    """

    prices = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                pass

    return prices


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
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)
