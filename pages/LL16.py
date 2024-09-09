import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL16")

st.write("##### CAS: [24703-35-3](https://scifinder-n.cas.org/searchDetail/substance/656068a925b43e48fca99692/substanceDetails)")
st.write("##### Gene No: LT14")
st.write("##### Compounds Name: Bicyclogermacrene")
st.write("##### 中文名: 双环吉马烯")
st.write("##### TPS original information: Ldu_C15-TPS08_Bicyclogermacrene_10.825min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.825")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.887686054")
st.write("##### Boiling Point: 267.8±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL16.png')
st.write("##### Mass spectrogram:")
st.image('image/LL16_MASS.png')
