import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL49")

st.write("##### CAS: No information")
st.write("##### Gene No: LT43")
st.write("##### Compounds Name: (1R,6S,7R,10R)-(+)-T-muurolol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Rca_C15-TPS50_(1R,6S,7R,10R)-(+)-T-muurolol_12.595min_NMR")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.595")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.96")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL49.png')
st.write("##### Mass spectrogram:")
st.image('image/LL49_MASS.png')
