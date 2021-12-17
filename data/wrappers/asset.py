class Asset(object):
    '''
    helper class

    manipulate data common to all assets:
    price and its derivatives

    '''
    # Assets: equity, FX, coin, 
    def __init__(self, ticker):
        self.ticker = ticker
        self.data_store = './data/local/store.h5'
        try:
            self.load_prices()
        except:
            print('Prices not fount, run fetch_prices()')

    def get_ticker(self):
        return self.ticker

    def load_prices(self):
        '''
        subclasses instantiate with reading data from the archive, price data location includes ticker and asset class
        messy?
        How to improve?
        '''
        import pandas as pd
        DATA_STORE = self.data_store
        with pd.HDFStore(DATA_STORE) as store:
            self.price_data = store[self.price_data_loc]

    def get_price_data(self):
        return self.price_data
    def set_price_data(self, df):
        self.price_data = df
    def save_prices_to_dataset(self):
        import pandas as pd
        df = self.price_data 
        DATA_STORE = self.data_store
        with pd.HDFStore(DATA_STORE) as store:
            store.put(self.price_data_loc, df)

    def set_momentum(self, col = 'returns'):
        #assert self.prices, pd.DataFrame
        data = self.price_data.loc[:,col]

        from talib import BBANDS, RSI
        self.momentum = {
        'bbands' : BBANDS(data, timeperiod=21, nbdevup=2, nbdevdn=2,matype=0),
        'rsi' : RSI(data, timeperiod=14)
        }
        return self.momentum

    def get_momentum(self):
        return self.momentum


    def show_momentum(self,  col = 'returns'):

        data = self.price_data.loc[:, col]
        self.set_momentum(col)

        up,mid,low = self.momentum['bbands']
        rsi = self.momentum['rsi'] 
        import matplotlib.pyplot as plt
        figure, axis = plt.subplots(2, 1)
        for i in (data,up,mid,low):
            
            axis[0].plot(i)

        #axis[1].plot(data.pct_change())
        axis[1].plot(rsi)

        [axis[n].title.set_text(i) for n,i in enumerate(('bbands','rsi'))]
        figure.canvas.manager.set_window_title(f'{self.ticker}')
        #figure.title.set_text()

        plt.show()

