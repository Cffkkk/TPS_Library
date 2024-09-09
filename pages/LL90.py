import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL90")

st.write("##### CAS: [87-44-5](https://scifinder-n.cas.org/searchDetail/substance/65640a4faa727207d57058a4/substanceDetails)")
st.write("##### Gene No: LT69")
st.write("##### Compounds Name: β-Caryophyllene")
st.write("##### 中文名: β-石竹烯")
st.write("##### TPS original information: OsaTPS02_β-caryophyllene_9.895min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.895")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 118-119 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL90.png')
st.write("##### Mass spectrogram:")
st.image('image/LL90_MASS.png')
