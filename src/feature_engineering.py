import pandas as pd

def compute_rsi(data, window=14):
    delta = data["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def check_csv():
    df = pd.read_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL.csv")
    print("Columns in CSV:", df.columns)
    
def add_technical_indicators(df):
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["SMA_200"] = df["Close"].rolling(window=200).mean()
    df["RSI"] = compute_rsi(df)
    return df.dropna()

if __name__ == "__main__":
    check_csv()
    df = pd.read_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL.csv", parse_dates=["Date"], index_col="Date")
    print(df.head())
    df = add_technical_indicators(df)
    df.to_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL_processed.csv")
