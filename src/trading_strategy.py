import pandas as pd

def apply_trading_strategy(df):
    """
    Generate buy/sell signals based on SMA crossover.
    Buy when SMA_50 crosses above SMA_200.
    Sell when SMA_50 crosses below SMA_200.
    """
    df["Signal"] = 0
    df.loc[df["SMA_50"] > df["SMA_200"], "Signal"] = 1  # Buy
    df.loc[df["SMA_50"] < df["SMA_200"], "Signal"] = -1 # Sell
    return df

if __name__ == "__main__":
    df = pd.read_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL_processed.csv", parse_dates=["Date"], index_col="Date")
    df = apply_trading_strategy(df)
    df.to_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL_signals.csv")
    print("Trading strategy applied. Signals saved.")
