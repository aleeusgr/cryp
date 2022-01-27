def test_binance():
    from  data.sources.market import binance 
    client = binance.auth()
    info = client.get_all_tickers()
    print(type(info))
    assert isinstance(info, list)
def test_ff5():
    from  data.sources.fundamental.famafrench import five_factor
    import pandas as pd
    df = five_factor()
    assert isinstance(df, pd.DataFrame)

def test_yahoo():
    from data.primary import Equity
    s = Equity('IBM')
    import pandas as pd 
    assert isinstance(s.fetch_prices(), pd.DataFrame)


#def test_moex():
#    import data.sources.market.moex as mx
#    result = ()
#    it = mx.__dict__
#    for name in it:
#        testing = it[name]
#        if callable(testing):
#           print(f'testing {testing}')
#           result += it[name](),
#    assert all((type(i) for i in result)) != None
