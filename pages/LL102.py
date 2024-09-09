import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL102")

st.write("##### CAS: [115888-31-8](https://scifinder-n.cas.org/searchDetail/substance/656805daaa727207d5b7785e/substanceDetails)")
st.write("##### Gene No: LT81")
st.write("##### Compounds Name: 5-epi-Aristolochene")
st.write("##### 中文名: 马兜铃烯")
st.write("##### TPS original information: V5-1_5-epi-Aristolochene_10.670min_others")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.67")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 274.2±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL102.png')
st.write("##### Mass spectrogram:")
st.image('image/LL102_MASS.png')
