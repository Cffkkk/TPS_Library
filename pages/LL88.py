import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL88")

st.write("##### CAS: [2567930-96](https://scifinder-n.cas.org/searchDetail/substance/65640927aa727207d5703f3c/substanceDetails)")
st.write("##### Gene No: LT67")
st.write("##### Compounds Name: 5-epi-Jinkoheremol")
st.write("##### 中文名: 沉香雅槛蓝醇")
st.write("##### TPS original information: Cro_C15-TPS79_5-epi-jinkoheremol_12.72min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.72")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 303.5±11.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL88.png')
st.write("##### Mass spectrogram:")
st.image('image/LL88_MASS.png')
