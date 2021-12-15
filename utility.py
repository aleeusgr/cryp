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


def candles(df):
    '''
    input df, index = datetime, index name = ticker, OHLC columns with names capitalized,
    
    todo: 
    candle width is set to half day, redo
    auto width of the chart?
    
    https://docs.bokeh.org/en/latest/docs/gallery/candlestick.html
    '''
    from math import pi
    import pandas as pd
    from bokeh.plotting import figure, show

    inc = df.Close > df.Open
    dec = df.Open > df.Close
    # this needs fixing
    width =24*7*3600*1000 # 12*60*60*1000 # half day in ms

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    ticker = df.index.name
    p = figure(x_axis_type="datetime", tools=TOOLS, width=1500, title = f"{ticker} Candlestick")
    p.xaxis.major_label_orientation = pi/4
    p.grid.grid_line_alpha=0.3


    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(df.index[inc], width, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.index[dec], width, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="black")
    
    show(p)

