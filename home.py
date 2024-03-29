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

st.subheader("การประยุกต์ใช้งาน Manchine Learning บนเว็บ")
st.subheader("by พีรพล พูลตาล")
st.subheader("สาขาวิทยาการคอมพิวเตอร์")
st.subheader("คณะวิทยาศาสตร์และเทคโนโลยี")
st.subheader("มหาวิทยาลัยราชภัฏนครปฐม")

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/Statistic.py", label="การนำเสนอข้อมูลถั่วแห้งด้วยสถิติ", icon="➊")
st.page_link("pages/Chart.py", label="การนำเสนอข้อมูลถั่วแห้งด้วยจินตทัศน์ข้อมูล", icon="➋", disabled=False)
st.page_link("pages/KNNClassify.py", label="การนำเสนอการจำเเนกข้อมูลถั่วเเห้ง", icon="➌", disabled=False)
st.page_link("pages/DecisionTreeClassify.py", label="การนำเสนอการจำเเนก", icon="➍", disabled=False)
st.page_link("pages/RegressionPrediction.py", label="การจำเเนกข้อมูลด้วยเทคนิกRegression", icon="➎", disabled=False)
st.page_link("pages/NaivebayeClassify.py", label="การจำเเนกข้อมูลด้วยเทคนิกNaivebaye", icon="➏", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")
