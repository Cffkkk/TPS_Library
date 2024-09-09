import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL55")

st.write("##### CAS: [20085-93-2](https://scifinder-n.cas.org/searchDetail/substance/65608f7225b43e48fcac9532/substanceDetails)")
st.write("##### Gene No: LT48")
st.write("##### Compounds Name: Seychellene")
st.write("##### 中文名: 西车烯")
st.write("##### TPS original information: Pca_C15-TPS58_Seychellene_10.330min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.33")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 250.6±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL55.png')
st.write("##### Mass spectrogram:")
st.image('image/LL55_MASS.png')
