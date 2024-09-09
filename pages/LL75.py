import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL75")

st.write("##### CAS: [10219-75-7](https://scifinder-n.cas.org/searchDetail/substance/656405e0aa727207d56ff7f8/substanceDetails)")
st.write("##### Gene No: LT60")
st.write("##### Compounds Name: (-)-Eremophilene")
st.write("##### 中文名: 佛术烯")
st.write("##### TPS original information: Osa_TPS07_(-)-eremophilene_10.74min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.74")
st.write("##### Formula:  C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 129.5 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL75.png')
st.write("##### Mass spectrogram:")
st.image('image/LL75_MASS.png')
