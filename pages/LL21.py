import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL21")

st.write("##### CAS: [5937/11/1](https://scifinder-n.cas.org/searchDetail/substance/656069a425b43e48fca9ace5/substanceDetails)")
st.write("##### Gene No: LT19")
st.write("##### Compounds Name: τ-Cadinol")
st.write("##### 中文名: 杜松醇")
st.write("##### TPS original information: Zma_C15-TPS14_Tau-cadinol_12.555min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.555")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.213373636")
st.write("##### Boiling Point: 303.4±31.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL21.png')
st.write("##### Mass spectrogram:")
st.image('image/LL21_MASS.png')
