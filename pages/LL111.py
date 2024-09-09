import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL111")

st.write("##### CAS: [28976-67-2](https://scifinder-n.cas.org/searchDetail/substance/656806e4aa727207d5b78949/substanceDetails)")
st.write("##### Gene No: LT90")
st.write("##### Compounds Name: β-Curcumene")
st.write("##### 中文名: β-姜黄烯")
st.write("##### TPS original information: V5-10_β-Curcumene_10.905min_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.905")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 128-130 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL111.png')
st.write("##### Mass spectrogram:")
st.image('image/LL111_MASS.png')
