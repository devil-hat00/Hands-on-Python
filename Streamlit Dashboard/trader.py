import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import ta

st.set_page_config(
    page_title="TraderIQ - Advanced Stock Analytics",
    layout="wide",
)

st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: 900;
    color: #2E86C1;
}
.subtle {
    font-size: 18px;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>TraderIQ — Advanced Stock Analytics Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtle'>Smart insights. Clean charts. Professional analytics.</div>", unsafe_allow_html=True)
st.write("---")

np.random.seed(42)

days = 180
dates = pd.date_range(start="2024-01-01", periods=days, freq="D")

price = 150 + np.cumsum(np.random.normal(0, 1.5, days))
high = price + np.random.uniform(0.5, 2, days)
low = price - np.random.uniform(0.5, 2, days)
open_ = price + np.random.uniform(-1, 1, days)
close = price
volume = np.random.randint(900, 6000, days)

df = pd.DataFrame({
    "Date": dates,
    "Open": open_,
    "High": high,
    "Low": low,
    "Close": close,
    "Volume": volume
}).set_index("Date")

st.sidebar.title("⚙️ Controls")

chart_type = st.sidebar.selectbox("Chart Type", ["Candlestick", "Line Chart"])

ma_window = st.sidebar.slider("MA Window", 5, 50, 20)
show_ma = st.sidebar.checkbox("Show Moving Average", True)

show_rsi = st.sidebar.checkbox("Show RSI", True)
show_macd = st.sidebar.checkbox("Show MACD", True)
show_boll = st.sidebar.checkbox("Show Bollinger Bands", True)

boll_window = st.sidebar.slider("Bollinger Window", 10, 40, 20)
boll_dev = st.sidebar.slider("Std Dev", 1, 3, 2)

df[f"MA_{ma_window}"] = df["Close"].rolling(ma_window).mean()

df["RSI"] = ta.momentum.RSIIndicator(df["Close"], fillna=True).rsi()

macd = ta.trend.MACD(df["Close"], fillna=True)
df["MACD_Line"] = macd.macd()
df["MACD_Signal"] = macd.macd_signal()
df["MACD_Hist"] = macd.macd_diff()

boll = ta.volatility.BollingerBands(df["Close"], window=boll_window, window_dev=boll_dev, fillna=True)
df["Boll_Upper"] = boll.bollinger_hband()
df["Boll_Lower"] = boll.bollinger_lband()

insights = []

if df["Close"].iloc[-1] > df[f"MA_{ma_window}"].iloc[-1]:
    insights.append("Market in Uptrend (Price above MA)")
else:
    insights.append("Market in Downtrend (Price below MA)")

rsi_val = df["RSI"].iloc[-1]
if rsi_val > 70:
    insights.append("Overbought — Possible Sell Reversal")
elif rsi_val < 30:
    insights.append("Oversold — Possible Buy Opportunity")
else:
    insights.append("RSI Neutral")

if df["MACD_Hist"].iloc[-1] > 0:
    insights.append("MACD Bullish Momentum Rising")
else:
    insights.append("MACD Bearish Momentum Dominant")

volatility_range = df["Boll_Upper"].iloc[-1] - df["Boll_Lower"].iloc[-1]
if volatility_range > 8:
    insights.append("High Volatility — Price swings are large")
else:
    insights.append("Low Volatility — Stable movement")

st.subheader("Market Price Chart")

if chart_type == "Candlestick":
    add_plots = []
    if show_ma:
        add_plots.append(mpf.make_addplot(df[f"MA_{ma_window}"], color="blue"))
    if show_boll:
        add_plots.append(mpf.make_addplot(df["Boll_Upper"], color="green"))
        add_plots.append(mpf.make_addplot(df["Boll_Lower"], color="green"))

    fig, ax = mpf.plot(
        df,
        type="candle",
        style="charles",
        volume=True,
        addplot=add_plots,
        figsize=(12, 6),
        returnfig=True
    )
    st.pyplot(fig)

else:
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.plot(df.index, df["Close"], label="Close", linewidth=2)

    if show_ma:
        ax.plot(df.index, df[f"MA_{ma_window}"], label=f"{ma_window}-MA", linewidth=1.5)

    if show_boll:
        ax.plot(df.index, df["Boll_Upper"], linestyle="--")
        ax.plot(df.index, df["Boll_Lower"], linestyle="--")

    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)


st.write("---")
st.subheader("Technical Indicators")

if show_rsi:
    st.write("RSI")
    fig, ax = plt.subplots(figsize=(13, 3))
    ax.plot(df.index, df["RSI"], color="purple")
    ax.axhline(70, color="red", linestyle="--")
    ax.axhline(30, color="green", linestyle="--")
    st.pyplot(fig)

if show_macd:
    st.write("MACD")
    fig, ax = plt.subplots(figsize=(13, 3))
    ax.plot(df.index, df["MACD_Line"], label="MACD", color="blue")
    ax.plot(df.index, df["MACD_Signal"], label="Signal", color="orange")
    ax.bar(df.index, df["MACD_Hist"], alpha=0.5)
    ax.legend()
    st.pyplot(fig)

st.write("---")
st.subheader("TraderIQ Smart Insights")

for i in insights:
    st.write(i)

st.write("---")
st.subheader("Market Data")

st.dataframe(df.tail(50))
