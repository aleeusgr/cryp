# cryp, Roadmap

###Backtest:
* run
* custom bundle
* custom strategy: Feng&Yulong

### F&Y
* momentum: which?
* investor attention

## Data, sources
Macro datasets? <br>
remember notes on /fin: data sources and datasets. 
HDF5?? 
### Fundamental
* pandas_datareader Fama/French reg: OK
* smartlab/interfax
* yahoo_fin: OK

### Market
* MOEX: apimoex, change to pdr??
* binance: OK
* quandl: OK #reduce read time for asset.h5

### Alt
* sentiment
* alt data for crypto?

## Data, Cleaning:
* pandas: OK
* /data/local/dt.py
* denoising: pykalman, fourier

## Feature Engineering
* momentum: OK
* value, investment, QmJ, # T/S momentum, Moscowitz 2012
* damodaran, : sector performance
* remember Factor Zoo.

## T/S analysis: 
// see montgomery, 2008
* stumpy
* ARCH, ARIMA
* neural prohet
* PyMC3, autoregressive

## Models:
* FF5 for moex?
* heterogeneous agent, Hommes
* representativeness, 
* network effects: search  

## Backtesting
* Zipline: custom data ingestion.
* backtesting.py: OK
* fixed time horizon performance vs entry point estimation
Z or B?
* Qlib, FinRL??

