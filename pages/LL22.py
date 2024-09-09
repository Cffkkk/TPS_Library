import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL22")

st.write("##### CAS: [19903-73-2](https://scifinder-n.cas.org/searchDetail/substance/656069ca25b43e48fca9b08d/substanceDetails)")
st.write("##### Gene No: LT20")
st.write("##### Compounds Name: (-)-8-epi-Cedrol")
st.write("##### 中文名: 异雪松醇")
st.write("##### TPS original information: Aan_C15-TPS16_(-)-8-epi-Cedrol_12.45min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 12.45")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.285338152")
st.write("##### Boiling Point: 277.2±8.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL22.png')
st.write("##### Mass spectrogram:")
st.image('image/LL22_MASS.png')
