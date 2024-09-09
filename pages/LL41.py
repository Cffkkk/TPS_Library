import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL41")

st.write("##### CAS: [35727-45-8](https://scifinder-n.cas.org/searchDetail/substance/6560724525b43e48fcaa74c5/substanceDetails)")
st.write("##### Gene No: LT36")
st.write("##### Compounds Name: Shyobunol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Spr_C15-TPS41_Shyobunol_11.115min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.115")
st.write("##### Formula: C15H26O2")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 272.3±39.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL41.png')
st.write("##### Mass spectrogram:")
st.image('image/LL41_MASS.png')
