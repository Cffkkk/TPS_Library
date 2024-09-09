import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL92")

st.write("##### CAS: [243663-91-4](https://scifinder-n.cas.org/searchDetail/substance/65640aa0aa727207d570609b/substanceDetails)")
st.write("##### Gene No: LT71")
st.write("##### Compounds Name: Presilphiperfol-1-ene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Cgl_Cgl06493-COP_Presilphiperfol-1-ene_8.58min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 8.58")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 259.9±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL92.png')
st.write("##### Mass spectrogram:")
st.image('image/LL92_MASS.png')
