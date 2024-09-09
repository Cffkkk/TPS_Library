import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL106")

st.write("##### CAS: [2415492-56-5](https://scifinder-n.cas.org/searchDetail/substance/65680727aa727207d5b78db4/substanceDetails)")
st.write("##### Gene No: LT85")
st.write("##### Compounds Name: Bungoene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: V5-12_Bungoene_9.920min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.92")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 260.3±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL106.png')
st.write("##### Mass spectrogram:")
st.image('image/LL106_MASS.png')
