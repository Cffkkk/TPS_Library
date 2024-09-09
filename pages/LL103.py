import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL103")

st.write("##### CAS: No information")
st.write("##### Gene No: LT82")
st.write("##### Compounds Name: Protoillud-7-ene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: V5-5_Protoillud-7-ene_8.835min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 8.835")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.96")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL103.png')
st.write("##### Mass spectrogram:")
st.image('image/LL103_MASS.png')
