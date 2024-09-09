import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL25")

st.write("##### CAS: [176589-53-0](https://scifinder-n.cas.org/searchDetail/substance/65606a8e25b43e48fca9c3b0/substanceDetails)")
st.write("##### Gene No: LT23")
st.write("##### Compounds Name: 10-epi-Cubebol")
st.write("##### 中文名: 荜澄茄醇")
st.write("##### TPS original information: Sce_C15-TPS20_10-epi-cubebol_11.245min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.245")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.86")
st.write("##### Boiling Point: 279.5±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL25.png')
st.write("##### Mass spectrogram:")
st.image('image/LL25_MASS.png')
