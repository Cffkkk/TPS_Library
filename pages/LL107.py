import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL107")

st.write("##### CAS: [1461-03-6](https://scifinder-n.cas.org/searchDetail/substance/656807c4aa727207d5b798f9/substanceDetails)")
st.write("##### Gene No: LT86")
st.write("##### Compounds Name: (+)-β-himachalene")
st.write("##### 中文名: (+)-Β-雪松烯")
st.write("##### TPS original information: V5-18_(+)-β-himachalene_10.865min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.865")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 132 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL107.png')
st.write("##### Mass spectrogram:")
st.image('image/LL107_MASS.png')
