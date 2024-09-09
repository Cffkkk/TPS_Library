import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL28")

st.write("##### CAS: No information")
st.write("##### Gene No: LT25")
st.write("##### Compounds Name: (+)-Corvol ether A")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Kse_C15-TPS22_(+)-corvoletherA_10.730min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.73")
st.write("##### Formula:  C15H26O")
st.write("##### Product proportion: 0.133405978")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL28.png')
st.write("##### Mass spectrogram:")
st.image('image/LL28_MASS.png')
