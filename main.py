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

#fama_french = ff5()
#start, end = (fama_french.index[i].strftime('%Y-%m-%d') for i in(0,-1))

class Equity(Asset):
    def __init(self,ticker):
        Asset.__init__(self,ticker)
        self.yahoo_data_loc =  f'pdr/yahoo/{ticker}'

    def fetch_yahoo(self, start = '2020-01-31', end = '2021-10-31' ):
        '''asset specific, use inheritance'''

        import pandas as pd
        import pandas_datareader as pdr
        df = pdr.DataReader(f'{self.ticker}', 'yahoo', start, end)
        df['returns'] = df['Adj Close'].pct_change()

        DATA_STORE = self.data_store
        with pd.HDFStore(DATA_STORE) as store:
            store.put(self.yahoo_data_loc, df)

    def load_yahoo(self):
        import pandas as pd
        DATA_STORE = self.data_store
        with pd.HDFStore(DATA_STORE) as store:
            self.yahoo_data = store[self.yahoo_data_loc]
    def get_yahoo_data(self):
        return self.yahoo_data

stock = Equity(dk_discount[0])
stock.load_yahoo()
