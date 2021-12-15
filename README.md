# cryp, Roadmap
1. decompose Equity, fetch -> data/sources/market/
2. tests for fetch
3. test Feng&Yulong

## Data, sources
Macro datasets? <br>
remember notes on /fin: data sources and datasets. 
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
* sklearn imputer
* fourier
* pykalman

## Feature Engineering
* momentum, value, investment, QmJ, # T/S momentum, Moscowitz 2012
* damodaran, : sector performance
* remember Factor Zoo.

## T/S analysis: 
// see montgomery, 2008
* stumpy
* ARCH, ARIMA
* neural prohet

## Models:
* FF5 for moex?
* heterogeneous agent, Hommes
* representativeness, 
* network effects: search  

## Backtesting
* Zipline: ingest binance.
* backtesting.py: OK
* fixed time horizon performance vs entry point estimation
Z or B?
* Qlib, FinRL??

## OrderExec:
* tinkoff_api.
* binance
