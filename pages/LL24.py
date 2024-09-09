import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL24")

st.write("##### CAS: [38230-60-3](https://scifinder-n.cas.org/searchDetail/substance/65606a0a25b43e48fca9b60a/substanceDetails)")
st.write("##### Gene No: LT22")
st.write("##### Compounds Name: 4-epi-Cubebol")
st.write("##### 中文名: 荜澄茄醇")
st.write("##### TPS original information: Sro_C15-TPS19_4-epi-cubebol_10.81min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.81")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.73")
st.write("##### Boiling Point: 279.5±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL24.png')
st.write("##### Mass spectrogram:")
st.image('image/LL24_MASS.png')
