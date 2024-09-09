import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL105")

st.write("##### CAS: [13062-00-5](https://scifinder-n.cas.org/searchDetail/substance/6568076daa727207d5b792af/substanceDetails)")
st.write("##### Gene No: LT84")
st.write("##### Compounds Name: (Z)-γ-Bisabolene")
st.write("##### 中文名: 红没药烯")
st.write("##### TPS original information: V5-17_(Z)-γ-Bisabolene_10.930min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.93")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 118-120 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL105.png')
st.write("##### Mass spectrogram:")
st.image('image/LL105_MASS.png')
