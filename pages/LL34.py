import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL34")

st.write("##### CAS: [473-15-4](https://scifinder-n.cas.org/searchDetail/substance/65606f9a25b43e48fcaa3aca/substanceDetails)")
st.write("##### Gene No: LT31")
st.write("##### Compounds Name: β-Eudesmol ")
st.write("##### 中文名: β-桉叶醇")
st.write("##### TPS original information: Zze_C15-TPS31_β-Eudesmol_12.77min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.77")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 301.7±11.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL34.png')
st.write("##### Mass spectrogram:")
st.image('image/LL34_MASS.png')
