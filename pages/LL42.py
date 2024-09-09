import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL42")

st.write("##### CAS: No information")
st.write("##### Gene No: LT36")
st.write("##### Compounds Name: 5,10-di-epi-shyobunol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Spr_C15-TPS41_5,10-di-epi-shyobunol_11.175min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.175")
st.write("##### Formula: C15H26O2")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL42.png')
st.write("##### Mass spectrogram:")
st.image('image/LL42_MASS.png')
