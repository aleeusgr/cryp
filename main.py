import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
#import pylab
#from  data.sources.market import moex, binance 
import pandas_datareader as pdr
#import pandas_ta as ta
import talib
from utility import *

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')

df = read_h5()
