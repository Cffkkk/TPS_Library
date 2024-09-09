import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL78")

st.write("##### CAS: No information")
st.write("##### Gene No: LT63")
st.write("##### Compounds Name: (-)-Acoradinene")
st.write("##### 中文名: 菖蒲二烯")
st.write("##### TPS original information: Fgr_FgFS_(-)-acoradinene_9.78min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.78")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: No information")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL78.png')
st.write("##### Mass spectrogram:")
st.image('image/LL78_MASS.png')
