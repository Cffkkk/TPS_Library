import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL112")

st.write("##### CAS: [6168-59-8](https://scifinder-n.cas.org/searchDetail/substance/65680058aa727207d5b71cc6/substanceDetails)")
st.write("##### Gene No: LT91")
st.write("##### Compounds Name: (+)-Intermedeol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: V5-15_(+)-Intermedeol_12.905min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.905")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.75")
st.write("##### Boiling Point: 298.5±19.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL112.png')
st.write("##### Mass spectrogram:")
st.image('image/LL112_MASS.png')
