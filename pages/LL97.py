import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL97")

st.write("##### CAS: No information")
st.write("##### Gene No: LT76")
st.write("##### Compounds Name: guaia-6,10(14)-diene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: FgJ02895_guaia-6,10(14)-diene_10.595min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.595")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL97.png')
st.write("##### Mass spectrogram:")
st.image('image/LL97_MASS.png')
