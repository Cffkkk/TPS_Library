import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL51")

st.write("##### CAS: No information")
st.write("##### Gene No: LT45")
st.write("##### Compounds Name: (S)-β-Macrocarpene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Zma_C15-TPS53_(S)-β-Macrocarpene_10.920min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.92")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL51.png')
st.write("##### Mass spectrogram:")
st.image('image/LL51_MASS.png')
