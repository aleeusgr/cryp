import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import talib
#import pylab
from  data.sources.market import binance 
#from  data.sources.fundamental.famafrench import five_factor
#import pandas_ta as ta
from data.primary import Equity, Coin
from data.wrappers.asset import Asset
from utility import  timer_func

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')
#stock = Equity(dk_discount[0])
coin = Coin('BNBBTC')

df = coin.get_price_data()
print(df.info())

#prices = pd.to_numeric(df.loc[:,'Close'])
#outlier_cutoff = 0.01 
#data = pd.DataFrame() 
#lags = [1, 2, 3, 6, 9, 12] 
#for lag in lags:
#    data[f'return_{lag}'] = prices.pct_change(lag)
