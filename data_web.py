#!bin/python
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
