import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL47")

st.write("##### CAS: [65372-78-3](https://scifinder-n.cas.org/searchDetail/substance/65608e1f25b43e48fcac7e65/substanceDetails)")
st.write("##### Gene No: LT41")
st.write("##### Compounds Name: α-Isocomene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Cre_C15-TPS47_α-Isocomene_9.505min_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.505")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 254.9±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL47.png')
st.write("##### Mass spectrogram:")
st.image('image/LL47_MASS.png')
