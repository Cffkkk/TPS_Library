import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL03")

st.write("##### CAS: [126-91-0](https://scifinder-n.cas.org/searchDetail/substance/6560196925b43e48fca2c2de/substanceDetails)")
st.write("##### Gene No: LT03")
st.write("##### Compounds Name: (-)-(3R)-Linalool")
st.write("##### 中文名: 芳樟醇")
st.write("##### TPS original information: Aan_C10-TPS08_(-)-(3R)-Linalool_5.37min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 5.37")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: 0.011613277")
st.write("##### Boiling Point: 80 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL03.png')
st.write("##### Mass spectrogram:")
st.image('image/LL03_MASS.png')
