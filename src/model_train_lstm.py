import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib

def train_lstm(symbol):
    df = pd.read_csv(f"../data/{symbol}_processed.csv", index_col="Date", parse_dates=True)
    
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df[["Close"]])
    
    X, y = [], []
    look_back = 30  # 30 days look-back period
    
    for i in range(look_back, len(df_scaled)):
        X.append(df_scaled[i-look_back:i])
        y.append(df_scaled[i])
    
    X, y = np.array(X), np.array(y)
    X_train, X_test, y_train, y_test = X[:-100], X[-100:], y[:-100], y[-100:]

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(look_back, 1)),
        LSTM(50),
        Dense(1)
    ])
    
    model.compile(loss="mse", optimizer="adam")
    model.fit(X_train, y_train, epochs=20, batch_size=16)

    model.save(f"../models/{symbol}_lstm.h5")
    joblib.dump(scaler, f"../models/{symbol}_scaler.pkl")

    print(f"LSTM model saved for {symbol}")

if __name__ == "__main__":
    train_lstm("AAPL")
