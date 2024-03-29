import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/377a24ee-4e19-48c9-8a2f-fcada962c70a/oax9riei3m.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello)

html_1 = """
<div style="background-color:#00FFFF;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลถั่วเเห้ง</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")