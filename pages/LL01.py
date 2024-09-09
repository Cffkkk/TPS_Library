import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL01")

st.write("##### CAS: [3779-61-1](https://scifinder-n.cas.org/searchDetail/substance/6560182925b43e48fca2ac94/substanceDetails)")
st.write("##### Gene No: LT01")
st.write("##### Compounds Name: (E)-β-Ocimene")
st.write("##### 中文名: 罗勒烯")
st.write("##### TPS original information: Ama_C10-TPS06_(E)-β-Ocimene_4.675min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 4.675")
st.write("##### Formula: C10H16")
st.write("##### Product proportion: 0.089656411")
st.write("##### Boiling Point: 175.2±10.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL01.png')
st.write("##### Mass spectrogram:")
st.image('image/LL01_MASS.png')
