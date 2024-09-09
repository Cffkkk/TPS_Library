import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL46")

st.write("##### CAS: No information")
st.write("##### Gene No: LT40")
st.write("##### Compounds Name: (2Z,4E)-α- Lonylideneethane")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Bfu_C15-TPS46_(2Z,4E)-α-Ionylideneethane_9.605min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.605")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.94")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL46.png')
st.write("##### Mass spectrogram:")
st.image('image/LL46_MASS.png')
