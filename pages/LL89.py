import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL89")

st.write("##### CAS: [62065-26-3](https://scifinder-n.cas.org/searchDetail/substance/65640968aa727207d5704537/substanceDetails)")
st.write("##### Gene No: LT68")
st.write("##### Compounds Name: Pentalenene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Sex_PentS_Pentalenene_8.825min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 8.825")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 262.5±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL89.png')
st.write("##### Mass spectrogram:")
st.image('image/LL89_MASS.png')
