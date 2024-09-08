import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL05")

st.write("##### CAS: [3387-41-5](https://scifinder-n.cas.org/searchDetail/substance/65601acb25b43e48fca2dc74/substanceDetails)")
st.write("##### Gene No: LT05")
st.write("##### Compounds Name: Sabinene")
st.write("##### 中文名: 桧烯")
st.write("##### TPS original information: Spo_C10_TPS16_Sabinene_3.870min_others")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 3.87")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: 0.245856753")
st.write("##### Boiling Point:  163-165 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL05.png')
st.write("##### Mass spectrogram:")
st.image('image/LL05_MASS.png')
