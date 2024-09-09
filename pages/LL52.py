import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL52")

st.write("##### CAS: [1119-38-6](https://scifinder-n.cas.org/searchDetail/substance/65608ecf25b43e48fcac89d5/substanceDetails)")
st.write("##### Gene No: LT46")
st.write("##### Compounds Name: (3S)-(E)-Nerolidol")
st.write("##### 中文名: 橙花叔醇")
st.write("##### TPS original information: Sfl_C15-TPS54_(3S)-(E)-Nerolidol_11.485min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.485")
st.write("##### Formula:  C15H26O")
st.write("##### Product proportion: 1.0")
st.write("##### Boiling Point: 113 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL52.png')
st.write("##### Mass spectrogram:")
st.image('image/LL52_MASS.png')
