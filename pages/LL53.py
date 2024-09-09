import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL53")

st.write("##### CAS: No information")
st.write("##### Gene No: LT47")
st.write("##### Compounds Name: (+)-(2S,3S,9R)-Pristinol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Spr_C15-TPS56_(+)-(2S,3S,9R)-pristinol_12.57min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.57")
st.write("##### Formula: C16H28O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL53.png')
st.write("##### Mass spectrogram:")
st.image('image/LL53_MASS.png')
