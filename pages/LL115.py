import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL115")

st.write("##### CAS: [3856-25-5](https://scifinder-n.cas.org/searchDetail/substance/65680655aa727207d5b77eb6/substanceDetails)")
st.write("##### Gene No: LT94")
st.write("##### Compounds Name: α-Copaene")
st.write("##### 中文名: Alpha-蒎烯")
st.write("##### TPS original information: V5-6_9.275min_α-Copaene_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.275")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 248.5 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL115.png')
st.write("##### Mass spectrogram:")
st.image('image/LL115_MASS.png')
