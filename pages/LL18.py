import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL18")

st.write("##### CAS: [76738-75-5](https://scifinder-n.cas.org/searchDetail/substance/6560691625b43e48fca9a09f/substanceDetails)")
st.write("##### Gene No: LT16")
st.write("##### Compounds Name: (+)-epi-α-Bisabolol")
st.write("##### 中文名: 红没药醇")
st.write("##### TPS original information: Ldu_C15-TPS11_(+)-epi-α-bisabolol_13.04min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 13.04")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.91")
st.write("##### Boiling Point: 314.5±11.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL18.png')
st.write("##### Mass spectrogram:")
st.image('image/LL18_MASS.png')
