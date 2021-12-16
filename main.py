import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import talib
#import pylab
#from  data.sources.market import moex, binance 
#from  data.sources.fundamental.famafrench import five_factor
#import pandas_ta as ta
from data.wrappers import Equity
from utility import  timer_func

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')

stock = Equity(dk_discount[0])


# momentum at the daily and weekly frequencies
stock.set_price_data(stock.get_price_data().resample('W').last())
data = stock.get_price_data().loc[:, 'returns']

up,mid,low = stock.set_momentum()['bbands']
figure, axis = plt.subplots(2, 1)
for i in (data,up,mid,low):
    
    axis[0].plot(i)

axis[1].plot(data.pct_change())


plt.show()

