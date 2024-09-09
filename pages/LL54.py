import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL54")

st.write("##### CAS: [3691/12/1](https://scifinder-n.cas.org/searchDetail/substance/65608f2125b43e48fcac8fde/substanceDetails)")
st.write("##### Gene No: LT48")
st.write("##### Compounds Name: α-Guaiene")
st.write("##### 中文名: α-布藜烯")
st.write("##### TPS original information: Pca_C15-TPS58_α-Guaiene_10.035min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.035")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 78-79 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL54.png')
st.write("##### Mass spectrogram:")
st.image('image/LL54_MASS.png')
