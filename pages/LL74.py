import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL74")

st.write("##### CAS: [4630/7/3](https://scifinder-n.cas.org/searchDetail/substance/6564059baa727207d56ff1cb/substanceDetails)")
st.write("##### Gene No: LT59")
st.write("##### Compounds Name: (+)-Valencene")
st.write("##### 中文名: 巴伦西亚橘烯")
st.write("##### TPS original information: Egl_EgVS_(+)-Valencene_10.805min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.805")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 123 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL74.png')
st.write("##### Mass spectrogram:")
st.image('image/LL74_MASS.png')
