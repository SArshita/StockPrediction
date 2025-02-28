import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_data(df, symbol="AAPL"):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price", color="blue")
    plt.plot(df.index, df["SMA_50"], label="SMA 50", color="green", linestyle="dashed")
    plt.plot(df.index, df["SMA_200"], label="SMA 200", color="red", linestyle="dashed")

    buy_signals = df[df["Signal"] == 1]
    sell_signals = df[df["Signal"] == -1]

    plt.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="green", label="Buy Signal", alpha=1)
    plt.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", label="Sell Signal", alpha=1)

    plt.title(f"{symbol} Stock Price with Trading Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL_signals.csv", parse_dates=["Date"], index_col="Date")
    plot_stock_data(df)
