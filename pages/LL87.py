import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL87")

st.write("##### CAS: [74841-87-5](https://scifinder-n.cas.org/searchDetail/substance/6564080eaa727207d57029bc/substanceDetails)")
st.write("##### Gene No: LT66")
st.write("##### Compounds Name: Germacrene-D-4-ol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Sit_C15-TPS78_germacrene-D-4-ol_11.8min_others")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.8")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 308.3±42.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL87.png')
st.write("##### Mass spectrogram:")
st.image('image/LL87_MASS.png')
