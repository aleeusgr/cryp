def test_moex():
    
    import pandas as pd
    import pandas_datareader as pdr
    f = pdr.get_data_moex(['USD000UTSTOM', 'MAGN'], '2020-07-02', '2020-07-07')
    assert isinstance(f, pd.DataFrame)

def test_yahoo():
    from data.wrappers.equity import Equity
    stock = Equity('IBM')
    import pandas as pd
    assert isinstance(stock.fetch_prices(), pd.DataFrame)
