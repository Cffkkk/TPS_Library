import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL59")

st.write("##### CAS: No information")
st.write("##### Gene No: LT49")
st.write("##### Compounds Name: Presilphiperfolan-8-β-ol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Bfu_C15-TPS60_Presilphiperfolan-8-β-ol_12.085min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.085")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.92")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL59.png')
st.write("##### Mass spectrogram:")
st.image('image/LL59_MASS.png')
