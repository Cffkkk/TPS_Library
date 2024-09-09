import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL69")

st.write("##### CAS: [28624-60-4](https://scifinder-n.cas.org/searchDetail/substance/6564051baa727207d56fe6f1/substanceDetails)")
st.write("##### Gene No: LT55")
st.write("##### Compounds Name: Trichodiene")
st.write("##### 中文名: 曲霉烯")
st.write("##### TPS original information: Fsp_C15-TPS66_Trichodiene_11.220min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.22")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.87")
st.write("##### Boiling Point: 256.7±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL69.png')
st.write("##### Mass spectrogram:")
st.image('image/LL69_MASS.png')
