import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL64")

st.write("##### CAS: [28624-23-9](https://scifinder-n.cas.org/searchDetail/substance/656092ce25b43e48fcaccd84/substanceDetails)")
st.write("##### Gene No: LT51")
st.write("##### Compounds Name: δ-Selinene")
st.write("##### 中文名: δ-芹子烯")
st.write("##### TPS original information: Pgr_C15-TPS62_δ-Selinene_10.680min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.68")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 282.9±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL64.png')
st.write("##### Mass spectrogram:")
st.image('image/LL64_MASS.png')
