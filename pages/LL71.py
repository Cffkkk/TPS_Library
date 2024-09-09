import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL71")

st.write("##### CAS: [495-60-3](https://scifinder-n.cas.org/searchDetail/substance/65640574aa727207d56fee83/substanceDetails)")
st.write("##### Gene No: LT57")
st.write("##### Compounds Name: Zingiberene")
st.write("##### 中文名: Α-姜烯")
st.write("##### TPS original information: Sbi_C15-TPS70_Zingiberene_10.725min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.725")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.64")
st.write("##### Boiling Point:  128-129 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL71.png')
st.write("##### Mass spectrogram:")
st.image('image/LL71_MASS.png')
