"""
	Explore yfinance and plotting time series
"""

# Import data manipulation libraries
import pandas as pd
import numpy as np

# Import yahoo finance library
import yfinance as yf

# Import cufflinks for visualization
import cufflinks as cf
cf.set_config_file(offline=True)

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

import plotly
# set this variable - to overcome 'plotly.offline' has no attribute error
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)

vix = yf.Ticker ("vix")
hist = vix.history(period="max")
interval = "1d"

vix = yf.download("^VIX", start="2006-01-01", end="2022-06-06")

# Manipulate the index to datetime from object
vix.index = pd.to_datetime(vix.index)

# Check the last five values
vix.tail()

#remove volume, we just want to plot volatility OHLC 
vix = vix.drop('Volume', 1)

# plot CBOE VIX data 
vix.iplot(kind='line', title='CBOE Volatily Index')

# unique years for which we have VIX data
years = vix.index.year.unique()
newdf = pd.DataFrame()

# just use VIX close values 
for year in years:
	newdf[year] = pd.Series(vix[vix.index.year==year]['Adj Close']).reset_index(drop=True)
vix.head()

newdf = newdf.ffill(axis=1)
newdf.head()

# print descriptive stats
newdf.describe().T

# now boxplot -- plot outliers
newdf.iloc[:,2:].iplot(kind='box', 
            title='CBOE Volatility Index', 
            yTitle='Annualised Volatility (%)', 
            legend=False, boxpoints='outliers')

