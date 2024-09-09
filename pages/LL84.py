import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL84")

st.write("##### CAS: [40716-66-3](https://scifinder-n.cas.org/searchDetail/substance/6564078daa727207d5701ea5/substanceDetails)")
st.write("##### Gene No: LT63")
st.write("##### Compounds Name: trans-Nerolidol")
st.write("##### 中文名: 反式橙花叔醇")
st.write("##### TPS original information: Fgr_FgFS_trans-nerolidol_11.485min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.485")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 113 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL84.png')
st.write("##### Mass spectrogram:")
st.image('image/LL84_MASS.png')
