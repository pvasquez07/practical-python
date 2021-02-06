# pcost.py
#
# Exercise 1.27
#
# pylint: disable=unused-variable
import sys
import csv
import report


def portfolio_cost(filename):
    """
    This function takes in a portfolio file and returns the total cost of the portfolio as a float.
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                numshares = int(record["shares"])
                purchaseprice = float(record["price"])
                total_cost += numshares * purchaseprice
                # This catches errors where int() or float() could not be converted.
            except ValueError:
                print(f"Row {rowno}: Couldn't covert: {row}")

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost", cost)
