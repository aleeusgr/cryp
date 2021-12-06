import pandas as pd
import numpy as np
import bokeh
import matplotlib.pyplot as plt
import pylab
from  data.sources.market import moex, binance 
import pandas_datareader as pdr

dk_discount = "IBM, ED, BEN, AFL, BDX, ADM, MMM, WBA, CAH, ABBV, SWK, ATO, NUE".split(sep = ', ')

#import
#tidy
#analyse: Viualise, Model, Transform
#hypothesis 
#

# Question, Research topic, Hypothesis, Test&Experiment, Analyse, Formulate. /Sci. method, Wikipedia
# Get data, define the investment universe, design factors, combine factors, optimize portfolio, exec orders. /Jensen

# factor construction: zvt,  ta, 
# momentum factor. 

class Asset(object):
    def __init__(self, symbol, start_date = "1 Jan 2021" , end_date = "1 Dec 2021", resolution = 'd'):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.resolution = resolution

