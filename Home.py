import streamlit as st
import pickle
from pathlib import Path

import streamlit_authenticator as stauth


## ----- User Auth ---
#name = ["Shadat Hossain","Shadat Patowary"]
#username = ["shadatH","shadatP"]

# Load hashed password
#file_path = Path(__file__).parent / "hashed_pw.pkl"
#with file_path.open("rb") as file:
#    hashed_password = pickle.load(file)
#authenticator = stauth.Authenticate(name,username,hashed_password,
#                                    "home","ajhksg", cookie_expiry_days=30)
#
#name,authentication_status,username = authenticator.login("Login","main")
#if authentication_status == False:
#    st.write("Username/Password is incorrect")
#if authentication_status == None:
#   st.write("Please enter your username and password")
#if authentication_status:
#    st.set_page_config(
#        page_title="Muiltipage App",
#        page_icon=":flag-bd:"
#    )
    ##authenticator.logout("Logout","sidebar")
st.set_page_config(
        page_title="Muiltipage App",
        page_icon=":flag-bd:"
    )