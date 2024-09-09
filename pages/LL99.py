import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL99")

st.write("##### CAS: [20307-84-0](https://scifinder-n.cas.org/searchDetail/substance/65645826aa727207d5779a32/substanceDetails)")
st.write("##### Gene No: LT78")
st.write("##### Compounds Name: δ-elemene")
st.write("##### 中文名: 榄香烯")
st.write("##### TPS original information: Sly_C15-TPS39_GermacreneC_8.705min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 8.705")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 254.5±40.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL99.png')
st.write("##### Mass spectrogram:")
st.image('image/LL99_MASS.png')
