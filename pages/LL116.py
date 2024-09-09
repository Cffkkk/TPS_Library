import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL116")

st.write("##### CAS: No information")
st.write("##### Gene No: LT95")
st.write("##### Compounds Name: (1S,6S,7R)-sesquipiperitol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: v5-30_12.980min_(1S,6S,7R)-sesquipiperitol_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.98")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL116.png')
st.write("##### Mass spectrogram:")
st.image('image/LL116_MASS.png')
