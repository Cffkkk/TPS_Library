import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL100")

st.write("##### CAS: [137941-79-8](https://scifinder-n.cas.org/searchDetail/substance/65655e32aa727207d5880f57/substanceDetails)")
st.write("##### Gene No: LT79")
st.write("##### Compounds Name: Vetispiradiene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Hmu_C15-TPS68_Vetispiradiene_10.920min")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.92")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 273.1±10.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL100.png')
st.write("##### Mass spectrogram:")
st.image('image/LL100_MASS.png')
