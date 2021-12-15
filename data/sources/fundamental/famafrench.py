def five_factor(start_date = '2000' ):
    '''
    start_date: str, 
    returns pd.DataFrame
    '''
    import pandas_datareader as pdr
    factors = ['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA']
    factor_data = pdr.DataReader('F-F_Research_Data_5_Factors_2x3','famafrench', start=start_date)[0].drop('RF', axis=1)
    factor_data.index = factor_data.index.to_timestamp()
    factor_data = factor_data.resample('M').last().div(100)
    factor_data.index.name = 'date'
    return factor_data
