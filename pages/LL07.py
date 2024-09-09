import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL07")

st.write("##### CAS: [99-85-4](https://scifinder-n.cas.org/searchDetail/substance/65601b3625b43e48fca2e292/substanceDetails)")
st.write("##### Gene No: LT07")
st.write("##### Compounds Name: γ-Terpinene")
st.write("##### 中文名:  γ-松油烯")
st.write("##### TPS original information: Cli_C10-TPS21_γ-terpinene_4.865min_standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 4.865")
st.write("##### Formula: C10H16")
st.write("##### Product proportion: 0.057091458")
st.write("##### Boiling Point: 183 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL07.png')
st.write("##### Mass spectrogram:")
st.image('image/LL07_MASS.png')
