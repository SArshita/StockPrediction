import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start="2020-01-01", end="2024-01-01"):
    df = yf.download(symbol, start=start, end=end)
    df.to_csv(f"../data/{symbol}.csv")
    df = pd.read_csv("../data/AAPL.csv")
    print(df.head())
    return df

if __name__ == "__main__":
    fetch_stock_data("AAPL")
