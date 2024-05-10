class Stock:
    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name

    def __str__(self):
        return f"{self.symbol}({self.company_name})"  