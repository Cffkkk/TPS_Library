import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL60")

st.write("##### CAS: [17066-67-0](https://scifinder-n.cas.org/searchDetail/substance/6560903425b43e48fcaca09d/substanceDetails)")
st.write("##### Gene No: LT50")
st.write("##### Compounds Name: β-Selinene")
st.write("##### 中文名: Β-瑟林烯")
st.write("##### TPS original information: Zma_C15-TPS61_β-Selinene_10.775min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.775")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.91")
st.write("##### Boiling Point: 120 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL60.png')
st.write("##### Mass spectrogram:")
st.image('image/LL60_MASS.png')
