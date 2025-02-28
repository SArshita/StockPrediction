import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Stock Prediction Dashboard")

# Load data
df = pd.read_csv("C:/Users/Arshita Satpute/Documents/2021-2025/Data Analytics/StockPrediction/data/AAPL_signals.csv", parse_dates=["Date"], index_col="Date")

st.title("📈 Stock Prediction & Trading Strategy")

# Plot stock price with moving averages
fig = px.line(df, x=df.index, y=["Close", "SMA_50", "SMA_200"], title="Stock Price & Moving Averages")
st.plotly_chart(fig)

# Show Buy/Sell signals
st.subheader("Buy/Sell Signals")
st.write("Buy: Green Triangle (▲), Sell: Red Triangle (▼)")

buy_signals = df[df["Signal"] == 1]
sell_signals = df[df["Signal"] == -1]

fig = px.scatter(df, x=df.index, y="Close", color=df["Signal"].map({1: "green", -1: "red", 0: "grey"}),
                 title="Trading Signals", labels={"color": "Signal"})

st.plotly_chart(fig)

st.write("📊 Data Preview:")
st.dataframe(df.head())
