import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL26")

st.write("##### CAS: [472-97-9](https://scifinder-n.cas.org/searchDetail/substance/65606ac525b43e48fca9c9ca/substanceDetails)")
st.write("##### Gene No: LT24")
st.write("##### Compounds Name: (+)-Caryolan-1-ol")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Sgr_C15-TPS21_(+)-Caryolan-1-ol_11.845min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.845")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.131305057")
st.write("##### Boiling Point: 295.0±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL26.png')
st.write("##### Mass spectrogram:")
st.image('image/LL26_MASS.png')
