import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL43")

st.write("##### CAS: [6753-98-6](https://scifinder-n.cas.org/searchDetail/substance/65608cd125b43e48fcac6512/substanceDetails)")
st.write("##### Gene No: LT37")
st.write("##### Compounds Name: α-Humulene")
st.write("##### 中文名: α-石竹烯/α-律草烯")
st.write("##### TPS original information: Zze_C15-TPS42_a-Humulene_10.35min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.35")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.94")
st.write("##### Boiling Point: 123 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL43.png')
st.write("##### Mass spectrogram:")
st.image('image/LL43_MASS.png')
