import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL12")

st.write("##### CAS: [39863-73-5](https://scifinder-n.cas.org/searchDetail/substance/656066c125b43e48fca96965/substanceDetails)")
st.write("##### Gene No: LT12")
st.write("##### Compounds Name: (-)-β-Barbatene")
st.write("##### 中文名: β-坝巴烷")
st.write("##### TPS original information: Ddi_C15-TPS06_(-)-β-Barbatene_10.325min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.325")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.594959582")
st.write("##### Boiling Point: 244.8±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL12.png')
st.write("##### Mass spectrogram:")
st.image('image/LL12_MASS.png')
