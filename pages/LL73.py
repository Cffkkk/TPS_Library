import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL73")

st.write("##### CAS: No information")
st.write("##### Gene No: LT58")
st.write("##### Compounds Name: (+)-Isozizaene")
st.write("##### 中文名: 异氮杂烯")
st.write("##### TPS original information: Czi_C15-TPS71_(+)-zizaene_10.405min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.405")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.72")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL73.png')
st.write("##### Mass spectrogram:")
st.image('image/LL73_MASS.png')
