import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL82")

st.write("##### CAS: [28296-85-7](https://scifinder-n.cas.org/searchDetail/substance/656406d1aa727207d5700e5f/substanceDetails)")
st.write("##### Gene No: LT63")
st.write("##### Compounds Name: (-)-α-Acorenol")
st.write("##### 中文名: 菖蒲醇")
st.write("##### TPS original information: Fgr_FgFS_(-)-α-Acorenol_12.50min_FgFS_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.5")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 312.2±11.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL82.png')
st.write("##### Mass spectrogram:")
st.image('image/LL82_MASS.png')
