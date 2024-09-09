import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL06")

st.write("##### CAS: [98-55-5](https://scifinder-n.cas.org/searchDetail/substance/65601aa525b43e48fca2d9e8/substanceDetails)")
st.write("##### Gene No: LT06")
st.write("##### Compounds Name: α-Terpinol")
st.write("##### 中文名: alpha-松油醇")
st.write("##### TPS original information: C10_TPS13_α-terpinol_6.750min_standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 6.75")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 218-221 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL06.png')
st.write("##### Mass spectrogram:")
st.image('image/LL06_MASS.png')
