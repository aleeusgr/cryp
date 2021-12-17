def test_Equity():

    from data.wrappers.equity import Equity
    s = Equity('IBM')
    import pandas as pd
    assert isinstance(s.get_price_data(),pd.DataFrame)


def test_tables():
    import pandas as pd
    DATA_STORE = './data/local/store.h5'

    with pd.HDFStore(DATA_STORE) as store:
        price_data = store
    assert isinstance(price_data, pd.io.pytables.HDFStore)
