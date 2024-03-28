import pandas as pd
import streamlit as st

dt=pd.read_excel'./data/Dry_Bean_Dataset.excel')
st.write(dt.head(16))
st.write(dt.describe())

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลถั่วเเห้ง</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)

st.markdown("")
st.write('ผลรวม')
cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8,cl9,cl10,cl11,cl12,cl13,cl14,cl15,cl16=st.columns(16)
cl1.write(dt['Area'].sum())
cl1.write(dt['Perimeter'].sum())
cl2.write(dt['MajorAxisLength'].sum())
cl3.write(dt['MinorAxisLength'].sum())
cl4.write(dt['AspectRation'].sum())
cl5.write(dt['Eccentricity'].sum())
cl6.write(dt['ConvexArea'].sum())
cl7.write(dt['EquivDiameter'].sum())
cl8.write(dt['Extent'].sum())
cl9.write(dt['Solidity'].sum())
cl10.write(dt['roundness'].sum())
cl11.write(dt['Compactness'].sum())
cl12.write(dt['ShapeFactor1'].sum())
cl13.write(dt['ShapeFactor2'].sum())
cl14.write(dt['ShapeFactor3'].sum())
cl15.write(dt['ShapeFactor4'].sum())
cl16.write(dt['Class'].sum())

