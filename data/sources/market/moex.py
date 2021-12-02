import apimoex as mx
import pandas as pd
import requests

def get_reference(n=0):
    '''
    placeholder reference by index. 

    '''
    with requests.Session() as session:
        place = ('engines,markets,boards,boardgroups,durations,securitytypes,securitygroups,securitycollections'.split(','))
        i = place[n]
        data = mx.get_reference(session,i) 
        #df = pd.DataFrame(data)
    return data

def get_tickers():
    '''
    Only works with default values
    full list of tickers.
    rewrite
    '''    
    engine = 'stock'
    market = 'shares'
    board = 'TQBR'
    request_url = ('https://iss.moex.com/iss/engines/{}/'
                   'markets/{}/boards/{}/securities.json'.format(engine,market,board))
    arguments = {'securities.columns': ('SECID,'
                                        'REGNUMBER,'
                                        'LOTSIZE,'
                                        'SHORTNAME')}
    with requests.Session() as session:
        iss = mx.ISSClient(session, request_url, arguments)
        data = iss.get()
        df = pd.DataFrame(data['securities'])
        #df.set_index('SECID', inplace=True)

        #df.to_csv('./data/moex_tickers.csv')
    return df
    
def get_history(ticker='SNGSP'):    
    '''rename, returns historical data for give ticker'''
    with requests.Session() as session:
        data = mx.get_board_history(session,ticker)
        df = pd.DataFrame(data)
        df.set_index('TRADEDATE', inplace=True)
    return df

def fetch_candles(ticker='SNGSP',start = '2021-01-13', cut = False, save = False): 
    '''rename, returns historical data for give ticker
    cut: return only data for specified col, rename col with ticker name'''
    with requests.Session() as session:

        data = mx.get_market_candles(session, security = ticker, start=start)

        df = pd.DataFrame(data)
        df['begin'] = pd.to_datetime(df['begin'])
        df.columns = df.columns.str.title()
        df.rename(columns = {'Value':'Volume', 'Begin': ticker}, inplace = True)
        df.set_index(ticker, inplace = True)
        if cut:
            df = df.rename(columns = {cut:ticker}) # this should be separate function
        if save:
            df.to_csv(f'./local/moex/{ticker}.csv')
    return df

