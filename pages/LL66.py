import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL66")

st.write("##### CAS: [159407-35-9](https://scifinder-n.cas.org/searchDetail/substance/6564039caa727207d56fc19d/substanceDetails)")
st.write("##### Gene No: LT53")
st.write("##### Compounds Name: 7-epi-Sesquithujene")
st.write("##### 中文名: (+)-7-表-倍半萜烯")
st.write("##### TPS original information: Zma_C15-TPS64_7-epi-sesquithujene_9.36min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.36")
st.write("##### Formula: C15H26")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 257.2±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL66.png')
st.write("##### Mass spectrogram:")
st.image('image/LL66_MASS.png')
