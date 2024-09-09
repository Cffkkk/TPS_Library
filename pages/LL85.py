import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL85")

st.write("##### CAS: No information")
st.write("##### Gene No: LT64")
st.write("##### Compounds Name: δ-Cubenol")
st.write("##### 中文名: 库贝醇/荜澄茄油烯醇 ")
st.write("##### TPS original information: Aae_C15-TPS73_δ-Cubenol_12.595min_standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.595")
st.write("##### Formula: C15H26O ")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL85.png')
st.write("##### Mass spectrogram:")
st.image('image/LL85_MASS.png')
