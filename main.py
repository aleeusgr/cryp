import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
#import pylab
#from  data.sources.market import moex, binance 
from  data.sources.famafrench import *
#import pandas_ta as ta
import pandas_datareader as pdr
import talib
from utility import *

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')
#stock = Asset(dk_discount[0])

#df = read_h5()
fama_french = ff5()

#price data
symbol = dk_discount[0]
start, end = (fama_french.index[i].strftime('%Y-%m-%d') for i in(0,-1))
df = pdr.DataReader(f'{symbol}', 'yahoo', start, end)
df = df.resample('M').last()
df['returns'] = df['Adj Close'].pct_change()

X = fama_french[:-1].to_numpy()
y = df.returns[1:].to_numpy()
import statsmodels.api as sm
X_ols = sm.add_constant(X)
model = sm.OLS(y, X_ols).fit()
print(model.summary())
