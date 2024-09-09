import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL14")

st.write("##### CAS: [82262-80-4](https://scifinder-n.cas.org/searchDetail/substance/6560679425b43e48fca97eb5/substanceDetails)")
st.write("##### Gene No: LT13")
st.write("##### Compounds Name: (+)-Thujopsene")
st.write("##### 中文名: 罗汉柏烯")
st.write("##### TPS original information: Ath_C15-TPS07_（+)-Thujopsene_10.115min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.115")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.335771513")
st.write("##### Boiling Point: 82262-80-4:256.5±7.0 °C(predicted) 470-40-6:120 °C(exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL14.png')
st.write("##### Mass spectrogram:")
st.image('image/LL14_MASS.png')
