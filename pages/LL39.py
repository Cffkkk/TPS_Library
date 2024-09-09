import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL39")

st.write("##### CAS: [3691-11-0](https://scifinder-n.cas.org/searchDetail/substance/656071b825b43e48fcaa681a/substanceDetails)")
st.write("##### Gene No: LT35")
st.write("##### Compounds Name: δ-Guaiene")
st.write("##### 中文名: δ-布藜烯")
st.write("##### TPS original information: Asp_C15-TPS36_δ-Guaiene_10.895min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.895")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.65")
st.write("##### Boiling Point: 274.5±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL39.png')
st.write("##### Mass spectrogram:")
st.image('image/LL39_MASS.png')
