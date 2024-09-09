import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL110")

st.write("##### CAS: No information")
st.write("##### Gene No: LT89")
st.write("##### Compounds Name: (+)-isodaucene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: V5-22_(+)-isodaucene_10.895min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.895")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.99")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL110.png')
st.write("##### Mass spectrogram:")
st.image('image/LL110_MASS.png')
