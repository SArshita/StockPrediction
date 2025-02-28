import pandas as pd
import joblib

def predict(symbol):
    model = joblib.load(f"C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/models/{symbol}_model.pkl")
    df = pd.read_csv(f"C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/{symbol}_processed.csv", index_col="Date", parse_dates=True)
    
    features = ["SMA_50", "SMA_200", "RSI", "Volume"]
    X = df[features].iloc[-1].values.reshape(1, -1)
    
    prediction = model.predict(X)
    return prediction[0]

if __name__ == "__main__":
    price = predict("AAPL")
    print(f"Predicted Price: {price}")
