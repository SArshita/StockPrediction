# Stock Prediction & Trading Strategy

This project predicts stock prices and generates buy/sell signals using machine learning.

## Features:
- Fetch historical stock data
- Compute technical indicators
- Train a predictive model
- Generate trading signals
- Visualize stock trends
- Interactive dashboard with Streamlit

## How to Run:
```bash
pip install -r requirements.txt
python src/data_loader.py
python src/feature_engineering.py
python src/model_train.py
python src/predict.py
python src/trading_strategy.py
python src/visualize.py
streamlit run webapp/app.py
