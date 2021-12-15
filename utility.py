def timer_func(func):
    ''' This function shows the execution time of 
    the function object passed
    https://www.geeksforgeeks.org/timing-functions-with-decorators-python/
    '''
    # assert callable?
    from time import time
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


#@timer_func


class Asset(object):
    '''
    data manipulation by asset
    ticker immutable

    '''
    # Assets: equity, FX, coin, 
    def __init__(self, ticker):
        self.ticker = ticker
        self.data_store = './data/local/store.h5'
        self.yahoo_data_loc =  f'pdr/yahoo/{ticker}'
    def get_ticker(self):
        return self.ticker


