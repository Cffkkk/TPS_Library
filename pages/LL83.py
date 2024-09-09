import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL83")

st.write("##### CAS: [23178-88-3](https://scifinder-n.cas.org/searchDetail/substance/65640771aa727207d5701c3c/substanceDetails)")
st.write("##### Gene No: LT63")
st.write("##### Compounds Name: (+)-α-Bisabolol")
st.write("##### 中文名: 红没药醇")
st.write("##### TPS original information: Fgr_FgFS_(+)-α-bisabolol_13.005min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 13.005")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 120-122 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL83.png')
st.write("##### Mass spectrogram:")
st.image('image/LL83_MASS.png')
