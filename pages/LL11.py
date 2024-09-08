import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL11")

st.write("##### CAS: [23515-88-0](https://scifinder-n.cas.org/searchDetail/substance/6560668925b43e48fca96448/substanceDetails)")
st.write("##### Gene No: LT11")
st.write("##### Compounds Name: (-)-α-Amorphene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Svi_C15-TPS03_(-)-α-Amorphene_10.6min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.6")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.420762614")
st.write("##### Boiling Point: 271.5±30.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL11.png')
st.write("##### Mass spectrogram:")
st.image('image/LL11_MASS.png')
