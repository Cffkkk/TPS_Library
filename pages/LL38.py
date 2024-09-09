import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL38")

st.write("##### CAS: No information")
st.write("##### Gene No: LT34")
st.write("##### Compounds Name:  5-Hydroxy-α-Gurjunene")
st.write("##### 中文名: 古芸烯")
st.write("##### TPS original information: Mpo_C15-TPS35_5-Hydroxy-α-Gurjunene_11.720min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.72")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL38.png')
st.write("##### Mass spectrogram:")
st.image('image/LL38_MASS.png')
