import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL67")

st.write("##### CAS: [495-61-4](https://scifinder-n.cas.org/searchDetail/substance/65640490aa727207d56fd912/substanceDetails)")
st.write("##### Gene No: LT53")
st.write("##### Compounds Name: (s)-β-Bisabolene")
st.write("##### 中文名: 红没药烯")
st.write("##### TPS original information: Zma_C15-TPS64_(s)-β-Bisabolene_10.89min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.89")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 145 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL67.png')
st.write("##### Mass spectrogram:")
st.image('image/LL67_MASS.png')
