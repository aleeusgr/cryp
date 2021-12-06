import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
#import pylab
from  data.sources.market import moex, binance 
import pandas_datareader as pdr
import pandas_ta as ta
import talib

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')
#import
#tidy
#analyse: Viualise, Model, Transform
#hypothesis 

# Question, Research topic, Hypothesis, Test&Experiment, Analyse, Formulate. /Sci. method, Wikipedia
# Get data, define the investment universe, design factors, combine factors, optimize portfolio, exec orders. /Jensen

# momentum, sentiment, value, volatility, size, quality
df = pd.DataFrame()
df = df.ta.ticker(dk_discount[0], period = '1y', interval = '1wk')
df = df.dropna()
output = talib.SMA(df.Close)

df.Close.plot()
output.plot()
plt.show()
