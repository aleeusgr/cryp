import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
#import pylab
from  data.sources.market import moex, binance 
import pandas_datareader as pdr

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')
#import
#tidy
#analyse: Viualise, Model, Transform
#hypothesis 

# Question, Research topic, Hypothesis, Test&Experiment, Analyse, Formulate. /Sci. method, Wikipedia
# Get data, define the investment universe, design factors, combine factors, optimize portfolio, exec orders. /Jensen

# momentum, sentiment, value, volatility, size, quality
import pandas_ta as ta
df = pd.DataFrame()
df = df.ta.ticker(dk_discount[0])
