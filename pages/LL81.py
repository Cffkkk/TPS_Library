import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL81")

st.write("##### CAS: No information")
st.write("##### Gene No: LT63")
st.write("##### Compounds Name: epi-Fusagramineol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Fgr_FgFS_epi-fusagramineol_11.885min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.885")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL81.png')
st.write("##### Mass spectrogram:")
st.image('image/LL81_MASS.png')
