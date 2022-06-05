"""
    This is a class for Options contract for pricing European options
	
"""
# Import required libraries
import pandas as pd
from numpy import *
from scipy.stats import norm

import matplotlib.pyplot as plt
from tabulate import tabulate

class BlackScholes:
	
	def __init__(self, spot, strike, rate, divYield, dte, volatility):
		
		self.spot = spot
		self.strike = strike
		self.rate = rate
		self.dte = dte
		self.volatility = volatility
		self.divYield = divYield
		
		self.d1 = (log (spot/strike) + (rate - divYield + square (volatility)/2) * dte) / (volatility * sqrt(dte))
		self.d2 = self.d1 - self.volatility * sqrt(self.dte)
		self.callPrice = self._price()

		
	def _price(self):
		_price = self.spot * exp (-1 *(self.divYield* self.dte)) * norm.cdf(self.d1) - self.strike * exp(-self.rate*self.dte)*norm.cdf(self.d2)
		return (_price)
	
		
## Call option
print ("Call option - Stock price:100, Strike: 110, Vol: 25% \n")
option = BlackScholes(100,100,0.05,.0,1,0.2)

header = ['Option Call Price', 'spot', 'strike']
table = [[option.callPrice, option.spot, option.strike]]
print(tabulate(table,header))