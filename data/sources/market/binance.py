
def read_key(file = 'binance'):
    key = {}
    with open(f'./data/keys/{file}') as f:
        content = f.read().splitlines()
        for i in content:
            x = i.split(sep = ': ')
            key[x[0]] = x[1]
    return key


def auth():
    key = read_key()

    from binance.client import Client
    api_key,api_secret = (i for i in key.values())

    client = Client(api_key, api_secret)
    
    return client

def fetch_candles(client, symbol ='BNBBTC' , start = '1 Nov 2021', end = '2 Nov 2021' ):
    ''' loads, names columns, saves locally
    datetime required in global frame
    returns nothin
    '''
    import pandas as pd
    import datetime
    limit = 500
    start_date = datetime.datetime.strptime(start, '%d %b %Y')
    end_date =   datetime.datetime.strptime(end, '%d %b %Y')

    columns  = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ]

    klines = client.get_historical_klines(symbol, client.KLINE_INTERVAL_1MINUTE, start_date.strftime('%d %b %Y %H:%M:%S'), end_date.strftime('%d %b %Y %H:%M:%S'), limit)
    data = pd.DataFrame(klines, columns = columns )
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

    data.set_index('timestamp', inplace=True)
    
    return data
