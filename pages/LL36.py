import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL36")

st.write("##### CAS: No information")
st.write("##### Gene No: LT33")
st.write("##### Compounds Name: (-)-5-epi-Eremophilene")
st.write("##### 中文名: 反式佛术烯")
st.write("##### TPS original information: Smi_C15-TPS33_(-)-5-Epieremophilene_10.74min_NMR")
st.write("##### Identification method in reference: Ref-Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.74")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL36.png')
st.write("##### Mass spectrogram:")
st.image('image/LL36_MASS.png')
