import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL93")

st.write("##### CAS: [18252-44-3](https://scifinder-n.cas.org/searchDetail/substance/65640af4aa727207d57068c6/substanceDetails)")
st.write("##### Gene No: LT72")
st.write("##### Compounds Name: β-Copaene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Cpu_Copu2_β-Copaene_10min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.0")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.612212384")
st.write("##### Boiling Point: 255.9±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL93.png')
st.write("##### Mass spectrogram:")
st.image('image/LL93_MASS.png')
