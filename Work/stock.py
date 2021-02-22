# stock.py


class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt


class MyStock(Stock):
    def cost(self):
        # Check the call to 'super'
        actual_cost = super().cost()
        return 1.25 * actual_cost
