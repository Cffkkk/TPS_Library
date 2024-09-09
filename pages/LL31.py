import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL31")

st.write("##### CAS: [1460-97-5](https://scifinder-n.cas.org/searchDetail/substance/65606b6525b43e48fca9dbf3/substanceDetails)")
st.write("##### Gene No: LT28")
st.write("##### Compounds Name: (-)-γ-Cadinene")
st.write("##### 中文名: 荜澄茄烯；杜松烯")
st.write("##### TPS original information: Cpi_C15-TPS27_(-)-γ-Cadinene_11.025min_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.025")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.85")
st.write("##### Boiling Point: 130-133 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL31.png')
st.write("##### Mass spectrogram:")
st.image('image/LL31_MASS.png')
