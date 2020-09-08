btc_dates = ["July 17, 2020", "July 18, 2020", "July 19, 2020", "July 20, 2020", "July 21, 2020", "July 22, 2020", "July 23, 2020", "July 24, 2020", "July 25, 2020", "July 26, 2020", "July 27, 2020", "July 28, 2020", "July 29, 2020", "July 30, 2020", "July 31, 2020"]
    #mmddyyyy
btc_opens = [9132, 9151, 9158, 9187, 9163, 9375, 9527, 9586, 9539, 9680, 9905, 11017, 10913, 11100, 11110]
    #July 17, 2020 - July 31, 2020 BTC Open Data(USD), rounded to nearest whole number
btc_closes = [9151, 9159, 9186, 9164, 9375, 9525, 9581, 9537, 9677, 9905, 10991, 10913, 11100, 11111, 11323]
    #July 17, 2020 - July 31, 2020 BTC Close Data(USD), rounded to nearest whole number
btc_highs = [9182, 9231, 9201, 9214, 9407, 9531, 9610, 9623, 9705, 10024, 11298, 11204, 11304, 11169, 11416]
    #July 17, 2020 - July 31, 2020 BTC Highs Data(USD), rounded to nearest whole number
btc_lows = [9089, 9101, 9098, 9138, 9149, 9320, 9483, 9481, 9530, 9653, 9904, 10633, 10856, 10895, 10987]
    #July 17, 2020 - July 31, 2020 BTC Lows Data(USD), rounded to nearest whole number

class BitcoinData:
    def __init__(self, btc_dates, btc_opens, btc_closes, btc_highs, btc_lows):
        self._btc_dates = btc_dates
        self._btc_opens = btc_opens
        self._btc_closes = btc_closes
        self._btc_highs = btc_highs
        self._btc_lows = btc_lows
    def btc_dates(self):
        return self._btc_dates
    def btc_opens(self):
        return self._btc_opens
    def btc_closes(self):
        return self._btc_closes
    def btc_highs(self):
        return self._btc_highs
    def btc_lows(self):
        return self._btc_lows
print(btc_dates)
print(btc_opens)
print(btc_closes)
print(btc_highs)
print(btc_lows)
#Two week period of Bitcoin Market Data, including the date, Open Prices, Close Prices, Highs, and Lows
