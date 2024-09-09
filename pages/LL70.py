import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL70")

st.write("##### CAS: [351222-66-7](https://scifinder-n.cas.org/searchDetail/substance/65640555aa727207d56feb6c/substanceDetails)")
st.write("##### Gene No: LT56")
st.write("##### Compounds Name: Valerena-4,7(11)-diene")
st.write("##### 中文名: 缬草-4,7（11）-二烯")
st.write("##### TPS original information: Vof_C15-TPS69_Valerena-4,7(11)-diene_10.230min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.23")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 272.7±10.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL70.png')
st.write("##### Mass spectrogram:")
st.image('image/LL70_MASS.png')
