from  data.sources.market import moex, binance 

client = binance.auth()
data = binance.fetch_candles(client)

