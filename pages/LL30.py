import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL30")

st.write("##### CAS: No information")
st.write("##### Gene No: LT27")
st.write("##### Compounds Name: (5S,7S,10R,11S)-Cucumene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Scl_C15-TPS26_(5S,7S,10R,11S)-cucumene_7.65min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 7.65")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.235053165")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL30.png')
st.write("##### Mass spectrogram:")
st.image('image/LL30_MASS.png')
