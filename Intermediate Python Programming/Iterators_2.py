if __name__ == '__main__':
    print("ok")


class Portfolio:
    def __init__(self):
        self.holdings = {'':''}  # key = ticker, Value = Shares


    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def iter(self):
        return iter(self.holdings.items())



myp = Portfolio()
myp.buy('Jmia', 30)
myp.buy('AQMS', 100)
myp.buy('VIAC', 200)
myp.buy('RIOT', 50)

print(myp)
print(type(myp))
print(type(Portfolio))

for (ticker, shares) in myp.items():
    print (ticker, shares)