import math

class Portfolio:

	def __init__(self, cash):
		self.cash = cash
		self.units = {}

	def buy(self, asset, price, weight):
		unit = math.floor((weight * self.cash) / price)
		if self.cash >= price * unit:
			self.cash = self.cash - (price * unit)
			self.units[asset] = (price, unit)
		else:
			print("NOT ENOUGH CASH! [Buy {} unit(s) of {}@{} FAILED]".format(unit, asset, price))

	def sell(self, asset, price):
		if asset in self.units:
			unit = self.units[asset][1]
			self.cash = self.cash + (price * unit)
			del self.units[asset]
		else:
			print("ASSET NOT FOUND! [Sell {}@{} FAILED]".format(asset, price))