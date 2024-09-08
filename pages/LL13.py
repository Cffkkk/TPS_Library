import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL13")

st.write("##### CAS: [53060-59-6](https://scifinder-n.cas.org/searchDetail/substance/6560671825b43e48fca9728d/substanceDetails)")
st.write("##### Gene No: LT13")
st.write("##### Compounds Name: (+)-α-Barbatene")
st.write("##### 中文名: α-坝巴烷")
st.write("##### TPS original information: Ath_C15-TPS07_(+)-α-Barbatene_9.885min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.885")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.33421753")
st.write("##### Boiling Point: 244.2±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL13.png')
st.write("##### Mass spectrogram:")
st.image('image/LL13_MASS.png')
