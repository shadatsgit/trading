import streamlit as st
import bybit
import apiConfig

client = bybit.bybit(test=False,api_key=apiConfig.api_key,api_secret=apiConfig.api_secret)

if client:
    st.title('Logged in')
else:
    st.write('Somthing Wrrong')