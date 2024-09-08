import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL15")

st.write("##### CAS: [15401-86-2](https://scifinder-n.cas.org/searchDetail/substance/6560687025b43e48fca99182/substanceDetails)")
st.write("##### Gene No: LT13")
st.write("##### Compounds Name: (+)-β-Chamigrene")
st.write("##### 中文名: 花柏烯")
st.write("##### TPS original information: Ath_C15-TPS07_(+)-β-Chamigrene_10.705min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.705")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.129934851")
st.write("##### Boiling Point: 273.2±20.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL15.png')
st.write("##### Mass spectrogram:")
st.image('image/LL15_MASS.png')
