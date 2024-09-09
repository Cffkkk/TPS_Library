import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL65")

st.write("##### CAS: [20307-83-9](https://scifinder-n.cas.org/searchDetail/substance/6564037baa727207d56fbddb/substanceDetails)")
st.write("##### Gene No: LT52")
st.write("##### Compounds Name: β-Sesquiphellandrene")
st.write("##### 中文名: 倍半菲兰烯/倍半水芹烯")
st.write("##### TPS original information: Sbi_C15-TPS63_β-Sesquiphellandrene_11.1min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.1")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.8")
st.write("##### Boiling Point: 90-90.5 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL65.png')
st.write("##### Mass spectrogram:")
st.image('image/LL65_MASS.png')
