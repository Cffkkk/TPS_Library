import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL48")

st.write("##### CAS: [465-24-7](https://scifinder-n.cas.org/searchDetail/substance/65608e5f25b43e48fcac829c/substanceDetails)")
st.write("##### Gene No: LT42")
st.write("##### Compounds Name:  Longiborneol")
st.write("##### 中文名: 长冰片醇")
st.write("##### TPS original information: Fgr_C15-TPS49_Longiborneol_12.2miin_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.2")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.82")
st.write("##### Boiling Point: 287.4±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL48.png')
st.write("##### Mass spectrogram:")
st.image('image/LL48_MASS.png')
