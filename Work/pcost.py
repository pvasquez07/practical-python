# pcost.py
#
# Exercise 1.27

import sys
import report


def portfolio_cost(filename):
    """
    This function takes in a portfolio file and returns the total cost of the portfolio as a float.
    """

    portfolio_cost = report.read_portfolio(filename)
    return sum([s.cost() for s in portfolio_cost])


def main(args):
    if len(args) != 2:
        raise SystemExit("Usage: %s portfile" % args[0])
    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":
    main(sys.argv)
