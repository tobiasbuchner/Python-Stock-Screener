from pytickersymbols import PyTickerSymbols
import pandas as pd

stock_data = PyTickerSymbols()
indices = stock_data.get_all_indices()
ticker_names = []
ticker_symbols = []
ticker_indices = []
ticker_industries = []
stock_indices = []
ticker_isins = []
for stock_index in indices:
    stocks = stock_data.get_stocks_by_index(stock_index)
    stocks = list(stocks)
    for ticker in stocks:
        ticker_names.append(ticker['name'])
        ticker_symbols.append(ticker['symbol'])
        ticker_indices.append(ticker['indices'])
        ticker_industries.append(ticker['industries'])
        ticker_isins.append(ticker['isins'])
        stock_indices.append(stock_index)
tickers_df = pd.DataFrame({'name': ticker_names, 'symbol': ticker_symbols,
                           'indices': ticker_indices,
                           'industries': ticker_industries,
                           'source_index': stock_indices,
                           'isins': ticker_isins})
# tickers_df.to_csv("./tickers.csv")

print(tickers_df)
