import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL94")

st.write("##### CAS: [512-61-8](https://scifinder-n.cas.org/searchDetail/substance/65640b8eaa727207d57072c6/substanceDetails)")
st.write("##### Gene No: LT73")
st.write("##### Compounds Name: α-Santalene")
st.write("##### 中文名: α-檀香烯")
st.write("##### TPS original information: Cla_SantS_α-santalene_9.81min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.81")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 262 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL94.png')
st.write("##### Mass spectrogram:")
st.image('image/LL94_MASS.png')
