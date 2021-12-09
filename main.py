import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
#import pylab
#from  data.sources.market import moex, binance 
import pandas_datareader as pdr
#import pandas_ta as ta
import talib
from utility import timer_func

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')
DATA_STORE = '~/workshop/machine-learning-for-trading/data/assets.h5'
START = 2011
END = 2018
idx =pd.IndexSlice
  

@timer_func
def read_h5():
    # exec time 39s from HDD, 25s from SSD
    with pd.HDFStore(DATA_STORE) as store:
        #prices = (store['quandl/wiki/prices'].loc[idx[str(START):str(END), :], 'adj_close'].unstack('ticker'))
        prices = None
        stocks = store['us_equities/stocks'].loc[dk_discount]# ['marketcap', 'ipoyear', 'sector']]
    return prices,stocks


prices, stocks = read_h5()
