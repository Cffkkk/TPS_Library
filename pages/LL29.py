import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL29")

st.write("##### CAS: [483-76-1](https://scifinder-n.cas.org/searchDetail/substance/65606b0925b43e48fca9d165/substanceDetails)")
st.write("##### Gene No: LT26")
st.write("##### Compounds Name: (+)-δ-Cadinene ")
st.write("##### 中文名: 荜澄茄烯；杜松烯")
st.write("##### TPS original information: Gna_C15-TPS23_(+)-δ-Cadinene_11.075min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.075")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 1.0")
st.write("##### Boiling Point: 279.7±15.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL29.png')
st.write("##### Mass spectrogram:")
st.image('image/LL29_MASS.png')
