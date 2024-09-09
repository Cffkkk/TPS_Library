import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL40")

st.write("##### CAS: [1816954-44-5](https://scifinder-n.cas.org/searchDetail/substance/656071f525b43e48fcaa6ce5/substanceDetails)")
st.write("##### Gene No: LT36")
st.write("##### Compounds Name: (+)-(1(10)E,4E,6S,7R)-Germacradien-6-ol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Spr_C15-TPS41_(+)-(1(10)E,4E,6S,7R)-Germacradien-6-ol_13.225min_NMR")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 13.225")
st.write("##### Formula: C15H26O2")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 320.4±42.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL40.png')
st.write("##### Mass spectrogram:")
st.image('image/LL40_MASS.png')
