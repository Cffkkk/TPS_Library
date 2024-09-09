import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL09")

st.write("##### CAS: [106-24-1](https://scifinder-n.cas.org/searchDetail/substance/6560639925b43e48fca91c42/substanceDetails)")
st.write("##### Gene No: LT09")
st.write("##### Compounds Name: Geraniol")
st.write("##### 中文名: 香叶醇")
st.write("##### TPS original information: Geraniol_7.405min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 7.405")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 230 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL09.png')
st.write("##### Mass spectrogram:")
st.image('image/LL09_MASS.png')
