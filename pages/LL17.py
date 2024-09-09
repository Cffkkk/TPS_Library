import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL17")

st.write("##### CAS: [25532-79-0](https://scifinder-n.cas.org/searchDetail/substance/656068ef25b43e48fca99ce8/substanceDetails)")
st.write("##### Gene No: LT15")
st.write("##### Compounds Name: (E)-α-Bisabolene")
st.write("##### 中文名: 红没药烯")
st.write("##### TPS original information: Agr_C15-TPS10_(E)-α-Bisabolene_11.28min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.28")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 1.0")
st.write("##### Boiling Point: 276.9±25.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL17.png')
st.write("##### Mass spectrogram:")
st.image('image/LL17_MASS.png')
