import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL109")

st.write("##### CAS: [123123-38-6](https://scifinder-n.cas.org/searchDetail/substance/6568083daa727207d5b7a11b/substanceDetails)")
st.write("##### Gene No: LT88")
st.write("##### Compounds Name: 7-epi-α-eudesmol")
st.write("##### 中文名: α-桉叶醇")
st.write("##### TPS original information: V5-20_7-epi-α-eudesmol_12.815min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.815")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.92")
st.write("##### Boiling Point: 301.1±11.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL109.png')
st.write("##### Mass spectrogram:")
st.image('image/LL109_MASS.png')
