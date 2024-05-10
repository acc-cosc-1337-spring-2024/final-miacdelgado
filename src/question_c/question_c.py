class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

class StockList:
    def __init__(self):
        self.stock_data = {
            "AAPL": "Apple Inc",
            "CAT": "Caterpillar",
            "EK": "Eastman Kodak",
            "GOOG": "Google",
            "MSFT": "Microsoft"
        }

    def display_stock_info(self):
        print("{:<10} {:<20}".format("Symbol", "Company Name"))
        for symbol, company_name in self.stock_data.items():
            print("{:<10} {:<20}".format(symbol, company_name))