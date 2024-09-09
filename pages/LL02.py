import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL02")

st.write("##### CAS: [126-90-9](https://scifinder-n.cas.org/searchDetail/substance/6560682925b43e48fca98b38/substanceDetails)")
st.write("##### Gene No: LT02")
st.write("##### Compounds Name: (3S)-Linalool")
st.write("##### 中文名: 芳樟醇")
st.write("##### TPS original information: Ath_C10-TPS07_(3S)-Linalool_5.375min_others")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 5.375")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: 0.032558777")
st.write("##### Boiling Point: 87-88 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL02.png')
st.write("##### Mass spectrogram:")
st.image('image/LL02_MASS.png')
