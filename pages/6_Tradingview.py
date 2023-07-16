import streamlit as st 
from tradingview_ta import TA_Handler,Interval,Exchange

symbols = ['AAPL','MSFT','TSLA','AMZN']

for symbol in symbols:
    output = TA_Handler(
        symbol=symbol,
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_5_MINUTES
    )
    st.title("Name : " + symbol)
    ##print(output.get_analysis().summary['RECOMMENDATION'])