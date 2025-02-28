import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Define full path for saving models
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction"))
MODELS_DIR = os.path.join(BASE_DIR, "models")  # Full path to models directory
DATA_DIR = os.path.join(BASE_DIR, "data")  # Full path to data directory

# Ensure models directory exists
os.makedirs(MODELS_DIR, exist_ok=True)

def load_data(symbol):
    """Load stock data from CSV"""
    file_path = os.path.join(DATA_DIR, f"{symbol}.csv")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    
    return df

def train_model(symbol):
    """Train a RandomForest model for the given stock symbol"""
    try:
        df = load_data(symbol)

        # Feature selection
        X = df[["High", "Low", "Open", "Volume"]]  # Features
        y = df["Close"]  # Target variable

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Model training
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Save trained model
        model_path = os.path.join(MODELS_DIR, f"{symbol}_model.pkl")
        with open(model_path, "wb") as file:
            pickle.dump(model, file)
        
        print(f"Model trained and saved successfully: {model_path}")

    except Exception as e:
        print(f"Error training model for {symbol}: {e}")

if __name__ == "__main__":
    stock_symbol = "AAPL"  # Change this to the stock symbol you're training
    train_model(stock_symbol)
