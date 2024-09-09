import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL57")

st.write("##### CAS: [514-51-2](https://scifinder-n.cas.org/searchDetail/substance/6560900525b43e48fcac9de9/substanceDetails)")
st.write("##### Gene No: LT48")
st.write("##### Compounds Name: β-Patchoulene")
st.write("##### 中文名: β-广藿香烯")
st.write("##### TPS original information: Pca_C15-TPS58_β-patchoulene_9.455min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.455")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 66.5-67.5 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL57.png')
st.write("##### Mass spectrogram:")
st.image('image/LL57_MASS.png')
