import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL63")

st.write("##### CAS: [36577-33-0](https://scifinder-n.cas.org/searchDetail/substance/65640365aa727207d56fbb43/substanceDetails)")
st.write("##### Gene No: LT51")
st.write("##### Compounds Name: Guaia-6,9-diene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Pga_C15-TPS62_Guaia-6,9-diene_10.100min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.1")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 273.4±15.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL63.png')
st.write("##### Mass spectrogram:")
st.image('image/LL63_MASS.png')
