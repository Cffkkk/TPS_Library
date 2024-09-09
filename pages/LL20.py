import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL20")

st.write("##### CAS: [15438-94-5](https://scifinder-n.cas.org/searchDetail/substance/6560696625b43e48fca9a774/substanceDetails)")
st.write("##### Gene No: LT18")
st.write("##### Compounds Name: (-)-β-trans-Bergamotene")
st.write("##### 中文名: 香柑油烯")
st.write("##### TPS original information: Afu_C15-TPS13_(-)-β-trans-Bergamotene_10.645min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.645")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 1.0")
st.write("##### Boiling Point: 260.1±7.0  °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL20.png')
st.write("##### Mass spectrogram:")
st.image('image/LL20_MASS.png')
