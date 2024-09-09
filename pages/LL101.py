import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL101")

st.write("##### CAS: No information")
st.write("##### Gene No: LT80")
st.write("##### Compounds Name: β-elemene/Germacrene A")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Lsa_LsLTC2_germacreneA_9.430min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.43")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL101.png')
st.write("##### Mass spectrogram:")
st.image('image/LL101_MASS.png')
