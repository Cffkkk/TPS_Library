import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL98")

st.write("##### CAS: [60305-17-1](https://scifinder-n.cas.org/searchDetail/substance/65640daeaa727207d5709905/substanceDetails)")
st.write("##### Gene No: LT77")
st.write("##### Compounds Name: (-)-δ-Cadinene")
st.write("##### 中文名: 杜松烯")
st.write("##### TPS original information: Scl_C15-TPS25_(-)-δ-Cadinene_11.085min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.075")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 279.7±15.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL98.png')
st.write("##### Mass spectrogram:")
st.image('image/LL98_MASS.png')
