import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL108")

st.write("##### CAS: No information")
st.write("##### Gene No: LT87")
st.write("##### Compounds Name: (4S,5S,7S)-discoidol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: V5-19_(4S,5S,7S)-discoidol_12.715min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.715")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL108.png')
st.write("##### Mass spectrogram:")
st.image('image/LL108_MASS.png')
