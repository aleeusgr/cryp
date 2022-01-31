def timer_func(func):
    ''' This function shows the execution time of 
    the function object passed
    https://www.geeksforgeeks.org/timing-functions-with-decorators-python/
    '''
    # assert is_callable(func)
    from time import time
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def read_portfolio():
    '''Import data from a proprietary excel file
    returns a list of tickers separated into boards (MOEX API term), with amount held at last rebalancing point. 
    '''
    import pandas as pd
    df = pd.read_excel('./data/local/portfolio.xlsx') # this can be done from the cloud
    select = df.iloc[:1,3:13] 
    select = select.T
    select.rename(columns = {0:'amount'},inplace = True)
    
    #FYI
    tickers = {
        'TQTF' : list(df.iloc[0,3:11].index),
        'TQTD' : list(df.iloc[0,11:13].index)
        }

    
    select['board'] = 'nul'

    for board in tickers.keys():
        select.loc[select.index.isin(tickers[board]), 'board'] = board
    return select

def fetch_portfolio():
    '''this depends on read_portfolio, they should be in a same module'''
    from data.sources.market import moex
    last_rebalance_date = '2021-01-13'
    portfolio = read_portfolio()
    data = {}
    #obtain data from the market
    for ticker in portfolio.index:

        board = portfolio.loc[ticker,'board']
         
        gh = moex.get_history(ticker, board, start = last_rebalance_date)
        data[ticker] = gh.loc[:,'CLOSE'] 
        
        price_data = pd.DataFrame(data)

    return price_data, portfolio 
