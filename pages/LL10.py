import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL10")

st.write("##### CAS: [123408-96-8](https://scifinder-n.cas.org/search/all/6560664d25b43e48fca95f8b)")
st.write("##### Gene No: LT10")
st.write("##### Compounds Name: Aristolochene")
st.write("##### 中文名: 马兜铃烯")
st.write("##### TPS original information: Agr_C15-TPS02_Aristolochene_10.710min_standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.71")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.96")
st.write("##### Boiling Point: 274.2±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL10.png')
st.write("##### Mass spectrogram:")
st.image('image/LL10_MASS.png')
