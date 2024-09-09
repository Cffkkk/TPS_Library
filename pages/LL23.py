import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL23")

st.write("##### CAS: [73694-25-4](https://scifinder-n.cas.org/searchDetail/substance/65606a3b25b43e48fca9ba5f/substanceDetails)")
st.write("##### Gene No: LT21")
st.write("##### Compounds Name: γ-Curcumene")
st.write("##### 中文名: γ-姜黄烯")
st.write("##### TPS original information: Pca_C15-TPS17_γ-Curcumene_10.51min")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.51")
st.write("##### Formula: C15H22")
st.write("##### Product proportion: 0.039361199")
st.write("##### Boiling Point: 94 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL23.png')
st.write("##### Mass spectrogram:")
st.image('image/LL23_MASS.png')
