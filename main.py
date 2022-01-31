import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
import pandas_datareader as pdr
#import talib
#import pylab
#from  data.sources.market import binance 
#from  data.sources.fundamental.famafrench import five_factor
#import pandas_ta as ta
from data.primary import Equity, Coin
from data.wrappers.asset import Asset
from utility import  timer_func, read_portfolio
from data.sources.market import moex


df = read_portfolio()

#obtain data from the market
t = 0
ticker = df.index[t]
board = df.iloc[t,1]

gh = moex.get_history(ticker, board)
