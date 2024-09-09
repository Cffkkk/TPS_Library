import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL114")

st.write("##### CAS: [142878-08-8](https://scifinder-n.cas.org/searchDetail/substance/656808c3aa727207d5b7a916/substanceDetails)")
st.write("##### Gene No: LT93")
st.write("##### Compounds Name: α-Cuprenene")
st.write("##### 中文名: Α-叩卜任烯")
st.write("##### TPS original information: v5-24_10.930min_α-Cuprenene_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.93")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 262.4±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL114.png')
st.write("##### Mass spectrogram:")
st.image('image/LL114_MASS.png')
