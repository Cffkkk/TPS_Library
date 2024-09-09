import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL33")

st.write("##### CAS: No information")
st.write("##### Gene No: LT30")
st.write("##### Compounds Name: dauca-4,7-diene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Ama_C15-TPS30_dauca-4,7-diene_11.585min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.585")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.98")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL33.png')
st.write("##### Mass spectrogram:")
st.image('image/LL33_MASS.png')
