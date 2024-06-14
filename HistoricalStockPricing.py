import pandas as pd
import yfinance as yf
import datetime
import numpy as np
import logging

ticker_symbols = pd.read_csv("tickers.csv")

logging.basicConfig(filename="logfilename.log", level=logging.INFO)
logging.info(str(datetime.datetime.now()))

open = []
date = []
high = []
low = []
close = []
adj_close = []
volume = []
ticker = []
date = []

for idx, symbol in enumerate(ticker_symbols['symbol']):
    print(symbol)
    print(idx)
    if isinstance(symbol, str):
        historical_pricing = yf.download(symbol, period='max').rename(
                            columns={'Adj Close': 'Adj_Close'})
        historical_pricing = historical_pricing.dropna(axis=1, how='all')
        if (historical_pricing.empty == False):
            historical_pricing = historical_pricing.assign(
                                Date=np.datetime_as_string(
                                    historical_pricing.index, unit='D'),
                                Ticker=symbol).set_index('Date')
            col_open = [col for col in historical_pricing.columns if "Open" in col]
            open.extend(historical_pricing[col_open[0]].tolist())
            col_low = [col for col in historical_pricing.columns if "Low" in col]
            low.extend(historical_pricing[col_low[0]].tolist())
            col_high = [col for col in historical_pricing.columns if "High" in col]
            high.extend(historical_pricing[col_high[0]].tolist())
            col_adj_close = [col for col in historical_pricing.columns if "Adj_Close" in col]
            adj_close.extend(historical_pricing[col_adj_close[0]].tolist())
            col_volume = [col for col in historical_pricing.columns if "Volume" in col]
            volume.extend(historical_pricing[col_volume[0]].tolist())
            col_ticker = [col for col in historical_pricing.columns if "Ticker" in col]
            ticker.extend(historical_pricing[col_ticker[0]].tolist())
            col_close = [col for col in historical_pricing.columns if "Close" in col]
            close.extend(historical_pricing[col_close[0]].tolist())
            date.extend(historical_pricing.index.tolist())
    else:
        logging.info(str(symbol))
historical_pricing_df = pd.DataFrame({'ticker': ticker,
                                      'date': date,
                                      'open': open,
                                      'high': high,
                                      'low': low,
                                      'close': close,
                                      'adj_close': adj_close,
                                      'volume': volume})
historical_pricing_df.to_csv("./historical_pricing.csv")
