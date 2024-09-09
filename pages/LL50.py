import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL50")

st.write("##### CAS: [10208-80-7](https://scifinder-n.cas.org/searchDetail/substance/65608e9d25b43e48fcac8669/substanceDetails)")
st.write("##### Gene No: LT44")
st.write("##### Compounds Name: α-Muurolene")
st.write("##### 中文名: α-衣兰油烯")
st.write("##### TPS original information: Cci_C15-TPS51_α-muurolene_10.830min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.83")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 118 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL50.png')
st.write("##### Mass spectrogram:")
st.image('image/LL50_MASS.png')
