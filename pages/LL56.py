import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL56")

st.write("##### CAS: [5986-55-0](https://scifinder-n.cas.org/searchDetail/substance/65608f9f25b43e48fcac9815/substanceDetails)")
st.write("##### Gene No: LT48")
st.write("##### Compounds Name: (-)-Patchoulol")
st.write("##### 中文名: 广藿香醇")
st.write("##### TPS original information: Pca_C15-TPS58_(-)-Patchoulol_13.035min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 13.035")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 287.4±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL56.png')
st.write("##### Mass spectrogram:")
st.image('image/LL56_MASS.png')
