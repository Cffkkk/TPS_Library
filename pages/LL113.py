import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL113")

st.write("##### CAS: No information")
st.write("##### Gene No: LT92")
st.write("##### Compounds Name: acora-4(14),8-diene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: v5-21_10.385min_acora-4(14),8-diene_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.385")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL113.png')
st.write("##### Mass spectrogram:")
st.image('image/LL113_MASS.png')
