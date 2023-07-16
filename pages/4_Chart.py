import streamlit as st
from datetime import datetime
import pandas as pd
from bokeh.plotting import figure,column

import talib
st.set_page_config(layout="wide",page_title="Candlestick Pattern Technical Analysis")

@st.cache_data
def load_dataset():
    btc_df = pd.read_csv("BTCUSD.csv", parse_dates=True)
    btc_df["Date"] = pd.to_datetime(btc_df["Date"])
    btc_df["BarColor"] = btc_df[["Open","Close"]].apply(lambda o: "red" if o.Open > o.Close else "green", axis=1)
    btc_df["Date_str"] = btc_df["Date"].astype(str)

    ## Calculate Various Indicators

    btc_df["SMA"] = talib.SMA(btc_df.Close, timeperiod=3)
    btc_df["MA"] = talib.MA(btc_df.Close, timeperiod=3)
    btc_df["EMA"] = talib.EMA(btc_df.Close, timeperiod=3)
    btc_df["WMA"] = talib.WMA(btc_df.Close, timeperiod=3)
    btc_df["RSI"] = talib.RSI(btc_df.Close, timeperiod=3)
    btc_df["MOM"] = talib.MOM(btc_df.Close, timeperiod=3)
    btc_df["DEMA"] = talib.DEMA(btc_df.Close, timeperiod=3)
    btc_df["TEMA"] = talib.TEMA(btc_df.Close, timeperiod=3)

    return btc_df 
btc_df = load_dataset()
indicator_color = {"SMA":"orange","EMA":"violet","WMA":"blue","RSI":"yellow","MOM":"black","DEMA":"red","MA":"tomato","TEMA":"dodgerblue"}

##Chart
def create_chart(df,close_line=False, include_vol=False,indicators=[]):
    ##Candlestick Pattern Logic
    candle = figure(x_axis_type="datetime",height=500,x_range=(df.Date.values[0],df.Date.values[-1]),
                    tooltips=[("Date","@Date_str"),("Open","@Open"),("High","@High"),("Low","@Low"),("Close","@Close")],
                    )
    candle.segment("Date","Low","Date","High",color="black",line_width=0.5,source=df)
    candle.segment("Date","Open","Date","Close",line_color="BarColor",line_width=2 if len(df)>100 else 6,source=df)

    candle.xaxis.axis_label="Date"
    candle.yaxis.axis_label="Price ($)"
    ##Close Price Line
    if close_line:
        candle.line("Date","Close",color="black",source=df)
    for indicator in indicators:
        candle.line("Date",indicator,color=indicator_color[indicator],line_width=2,source=df,legend_label=indicator )
    ##Volume Bars Logic
    volume = None
    if include_vol:
        volume = figure(x_axis_type="datetime",plot_height=150, x_range=(df.Date.values[0],df.Date.values[-1]),)
        volume.segment("Date",0,"Date","Volume", line_width=2 if len(df)>100 else 6, line_color="BarColor",alpha=0.8,source=df)
        volume.yaxis.axis_label="volume"

    return column(children=[candle,volume], sizing_mode="scale_width") if volume else candle

talib_indicators = ["MA","EMA","SMA","WMA","RSI","MOM","DEMA","TEMA"]

## Dashboard

st.title(":green[Candle]:red[stick] Pattern Technical Analysis :tea:")

st.sidebar.title('Date Rang Selection')

col1,col2 = st.sidebar.columns(2)
with col1:
    start_date = st.date_input(label="Start Date", value=datetime(2023,4,1))
with col2:
    end_date = st.date_input(label="End Date", value=datetime(2023,7,2))
sub_df = btc_df.set_index("Date").loc[str(start_date):str(end_date)]
sub_df = sub_df.reset_index()

close_line = st.sidebar.checkbox(label="Close Price")
volume = st.sidebar.checkbox(label="Include Trading Volume")

indicators = st.sidebar.multiselect(label="Technical Indicators", options=talib_indicators)

fig = create_chart(sub_df, close_line,volume,indicators)
st.bokeh_chart(fig, use_container_width=True)
