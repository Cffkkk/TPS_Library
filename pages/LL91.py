import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL91")

st.write("##### CAS: [18794-84-8](https://scifinder-n.cas.org/searchDetail/substance/65640a7aaa727207d5705c64/substanceDetails)")
st.write("##### Gene No: LT70")
st.write("##### Compounds Name: E-β-Farnesene")
st.write("##### 中文名: 反式-β-金合欢烯")
st.write("##### TPS original information: Mre_BFS_E-β-farnesene_10.14min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.14")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 80-82 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL91.png')
st.write("##### Mass spectrogram:")
st.image('image/LL91_MASS.png')
