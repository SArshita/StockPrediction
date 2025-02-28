import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(symbol):
    df = pd.read_csv(f"../data/{symbol}_processed.csv", index_col="Date", parse_dates=True)
    features = ["SMA_50", "SMA_200", "RSI", "Volume"]
    
    X = df[features]
    y = df["Close"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, f"../models/{symbol}_model.pkl")
    print(f"Model trained and saved for {symbol}")

if __name__ == "__main__":
    train_model("AAPL")
