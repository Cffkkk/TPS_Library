import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL76")

st.write("##### CAS: [1207718-51-1](https://scifinder-n.cas.org/searchDetail/substance/6564061aaa727207d56ffc10/substanceDetails)")
st.write("##### Gene No: LT61")
st.write("##### Compounds Name: epi-Isozizaene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Sco_5222_Epi-Isozizaene_10.25min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.25")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 268.9±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL76.png')
st.write("##### Mass spectrogram:")
st.image('image/LL76_MASS.png')
