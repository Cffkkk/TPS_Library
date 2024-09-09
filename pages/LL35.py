import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL35")

st.write("##### CAS: [1410797-90-8](https://scifinder-n.cas.org/searchDetail/substance/65606ff725b43e48fcaa4352/substanceDetails)")
st.write("##### Gene No: LT32")
st.write("##### Compounds Name: (+)-Eremophilene")
st.write("##### 中文名: 佛术烯")
st.write("##### TPS original information: Gfu_C15-TPS32_(+)-Eremophilene_10.740min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.74")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.92")
st.write("##### Boiling Point: 129.5 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL35.png')
st.write("##### Mass spectrogram:")
st.image('image/LL35_MASS.png')
