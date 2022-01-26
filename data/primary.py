from data.wrappers.asset import Asset

class Equity(Asset):
    def __init__(self,ticker):

        self.price_data_loc =  f'pdr/yahoo/{ticker}'
        Asset.__init__(self,ticker)
        try:
            self.load_prices()
            self.price_data['returns'] = self.price_data['Adj Close'].pct_change()
        except:
            print('run fetch_prices')

    def fetch_prices(self, start = '2020-01-31', end = '2021-10-31' ):
        '''load from web'''
        import pandas as pd
        import pandas_datareader as pdr
        if end == 'last':
            # end = datetime.today
            pass
        df = pdr.DataReader(f'{self.ticker}', 'yahoo', start, end)
        self.yahoo_data = df
        return df

class Coin(Asset):
    def __init__(self, ticker):

        self.price_data_loc =  f'binance/{ticker}'
        Asset.__init__(self,ticker) 
        self.load_prices()
        self.price_data['returns'] = self.price_data.loc[:,'Close']

    def fetch_prices(self, start = '2020-01-30', end = '2020-01-31' ):
        ''' loads, names columns,
        '''
        from  data.sources.market import binance 
        import pandas as pd
        import datetime
        self.client = binance.auth()
        date_format = '%Y-%m-%d'
        limit = 500
        start_date, end_date = [ datetime.datetime.strptime(i,date_format) for i in (start,end)]

        print(start_date,end_date)
        columns  = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ]

        klines = self.client.get_historical_klines(self.ticker, self.client.KLINE_INTERVAL_1MINUTE, start_date.strftime('%d %b %Y %H:%M:%S'), end_date.strftime('%d %b %Y %H:%M:%S'), limit)
        data = pd.DataFrame(klines, columns = columns )
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

        data.set_index('timestamp', inplace=True)
        self.price_data = data 
        return data
