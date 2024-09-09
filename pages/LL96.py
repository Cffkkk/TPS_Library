import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL96")

st.write("##### CAS: [72188-51-3](https://scifinder-n.cas.org/searchDetail/substance/65640ca0aa727207d570852d/substanceDetails)")
st.write("##### Gene No: LT75")
st.write("##### Compounds Name: Koraiol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: FgJ09920_koraiol_12.385min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.385")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 259.9±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL96.png')
st.write("##### Mass spectrogram:")
st.image('image/LL96_MASS.png')
