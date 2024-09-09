import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL86")

st.write("##### CAS: [23986-74-5](https://scifinder-n.cas.org/searchDetail/substance/656407e1aa727207d570262a/substanceDetails)")
st.write("##### Gene No: LT65")
st.write("##### Compounds Name: Germacrene D")
st.write("##### 中文名: 吉马烯D")
st.write("##### TPS original information: Sit_C15-TPS77_GermacreneD_10.635min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.635")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 279.7±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL86.png')
st.write("##### Mass spectrogram:")
st.image('image/LL86_MASS.png')
