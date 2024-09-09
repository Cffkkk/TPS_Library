import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL72")

st.write("##### CAS: No information")
st.write("##### Gene No: LT57")
st.write("##### Compounds Name: β-Sesquiphellandrene")
st.write("##### 中文名: 倍半菲兰烯/倍半水芹烯")
st.write("##### TPS original information: Sbi_C15-TPS70_β-sesquiPhellandrene_11.105min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.105")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL72.png')
st.write("##### Mass spectrogram:")
st.image('image/LL72_MASS.png')
