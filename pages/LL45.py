import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL45")

st.write("##### CAS: [104975-19-1](https://scifinder-n.cas.org/searchDetail/substance/65608d3525b43e48fcac6d0a/substanceDetails)")
st.write("##### Gene No: LT39")
st.write("##### Compounds Name: (+)-Isoafricanol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Spr_C15-TPS44_(+)-IIsoafricanol_11.300min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.3")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 287.4±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL45.png')
st.write("##### Mass spectrogram:")
st.image('image/LL45_MASS.png')
