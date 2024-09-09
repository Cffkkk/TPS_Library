import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL44")

st.write("##### CAS: [639-99-6/32142-08-8](https://scifinder-n.cas.org/searchDetail/substance/65608d0f25b43e48fcac69b5/substanceDetails)")
st.write("##### Gene No: LT38")
st.write("##### Compounds Name: Elemol")
st.write("##### 中文名: 己果醇")
st.write("##### TPS original information: Kse_C15-TPS43_(2Z,6E)-hedycaryol_11.425min")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.425")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.93")
st.write("##### Boiling Point: 152-156 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL44.png')
st.write("##### Mass spectrogram:")
st.image('image/LL44_MASS.png')
