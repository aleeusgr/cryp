
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
