import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL95")

st.write("##### CAS: No information")
st.write("##### Gene No: LT74")
st.write("##### Compounds Name: Protoilludene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Ool_OMP7_Protoilludene_9.295min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.295")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL95.png')
st.write("##### Mass spectrogram:")
st.image('image/LL95_MASS.png')
