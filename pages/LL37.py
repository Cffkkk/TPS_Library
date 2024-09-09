import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL37")

st.write("##### CAS: [489-40-7](https://scifinder-n.cas.org/searchDetail/substance/656070e925b43e48fcaa578f/substanceDetails)")
st.write("##### Gene No: LT34")
st.write("##### Compounds Name: α-Gurjunene")
st.write("##### 中文名: α-古芸烯")
st.write("##### TPS original information: Mpo_C15-TPS35_α-gurjunene_9.725min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.725")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 76-77 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL37.png')
st.write("##### Mass spectrogram:")
st.image('image/LL37_MASS.png')
