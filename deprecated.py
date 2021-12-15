
def read_h5_from_jensen(START = 2011,END = 2020):
    import pandas as pd
    DATA_STORE = '~/workshop/machine-learning-for-trading/data/assets.h5'
    idx =pd.IndexSlice
    with pd.HDFStore(DATA_STORE) as store:
        print(store.info()) 
        result = (store['quandl/wiki/prices'].loc[idx[str(START):str(END), :], 'adj_close'].unstack('ticker')) # exec time 39s from HDD, 25s from SSD
        #result = (store['engineered_features']) # time = 2.5s 
        #result = (store['quandl/wiki/stocks']) # is in us_equities/stocks
        #result = (store['sp500/fred']) #???

        # company info: age, market cap, HQ location, etc. 
        #result = (store['sp500/stocks']) # seems better then us_equities/stocks, but no market cap
        #result = store['us_equities/stocks']# ['marketcap', 'ipoyear', 'sector']] #time = 1s
    return  result
'''
REFACTOR: pandas_datareader, world_bank_data and other wrappers
'''

def fetch(save = False, dset_name = 'RUB'):
    '''Get data from web
     DO:
     decompose   
     try different sources
     parameters 

     resamples, saves to disk'''

    import pandas_datareader.data as web
    import datetime as dt
    import world_bank_data as wb

    #wb.get_topics()

    provider = {
    0:'yahoo',  # symbols: MSFT
    1:'quandl', #has specific symbol format. symbols:??? 
    2: 'moex',  #Moscow Exchange.  symbols:??? 
    3: 'fred',  #???
    4: 'stooq', #common index data. symbols: ^DJI
    5: 'eurostat', #browse website for symbols
    6: 'iex',   # requires API key
    }

    n_prov = 0
    symbols = {
    'yahoo' : ('rub','RUB=X')#  (('oil','CL=F'),
    }
    web_data = {}
    start = '1998-01-01' # train_y starts here 
    end_train = '2020-10-26' 
    name = 'rub'
    ticker = 'RUB=X'
    web_data[name] = web.DataReader(ticker,provider[n_prov],start=start) 
    web_data[name] = web_data[name].loc[:,'Close'].resample('1d').mean()
    web_data[name].fillna(method='bfill',inplace=True)
    
    import pandas as pd
    dset = pd.DataFrame.from_dict(web_data)
    lengths = dset.count(0)
    dset_cut = dset.iloc[lengths.max()-lengths.min():].copy()
    if save:
        dset_cut.to_csv('./data/{}.csv'.format(dset_name))
    return dset_cut

def loadX(save_locally = False, dset_name = 'dataset.csv'):
    import pandas as pd
    try:
        dataX = pd.read_csv(dset_name)
        #dataX = load_local_x()
    except:
        print('local files not found, fetching..')
        dataX = fetch(save_locally, dset_name = 'dataset.csv')
    return dataX

