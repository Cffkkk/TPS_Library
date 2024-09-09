import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL58")

st.write("##### CAS: [3691-11-0](https://scifinder-n.cas.org/searchDetail/substance/65608fd025b43e48fcac9ac7/substanceDetails)")
st.write("##### Gene No: LT48")
st.write("##### Compounds Name: α-Bulnesene")
st.write("##### 中文名: α-布藜烯")
st.write("##### TPS original information: Pca_C15-TPS58_α-bulnesene_10.895min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.895")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 274.5±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL58.png')
st.write("##### Mass spectrogram:")
st.image('image/LL58_MASS.png')
