import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL04")

st.write("##### CAS: [470-82-6](https://scifinder-n.cas.org/searchDetail/substance/6560199825b43e48fca2c5f1/substanceDetails)")
st.write("##### Gene No: LT04")
st.write("##### Compounds Name: 1,8-Cineole")
st.write("##### 中文名: 桉树醇")
st.write("##### TPS original information: Cuu_C10-TPS11_1,8-Cineole_4.6min_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 4.6")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: 0.072050493")
st.write("##### Boiling Point: 176.4 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL04.png')
st.write("##### Mass spectrogram:")
st.image('image/LL04_MASS.png')
