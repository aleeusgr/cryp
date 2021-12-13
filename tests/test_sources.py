def test_moex():
    import data.sources.market.moex as mx
    result = ()
    it = mx.__dict__
    for name in it:
        testing = it[name]
        if callable(testing):
           print(f'testing {testing}')
           result += it[name](),
    assert all((type(i) for i in result)) != None
    
def test_binance():
    
    import pandas as pd
    from  data.sources.market import  binance 
    import datetime
    print('datetime import required to run, fix')
    client = binance.auth()
    data = binance.fetch_candles(client)
    assert isinstance(data, pd.DataFrame)

def test_ff5():
    from  data.sources.famafrench import ff5
    import pandas as pd
    df = ff5()
    assert isinstance(df, pd.DataFrame)
