import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL32")

st.write("##### CAS: [468-68-8](https://scifinder-n.cas.org/searchDetail/substance/65606b8925b43e48fca9e0bb/substanceDetails)")
st.write("##### Gene No: LT29")
st.write("##### Compounds Name: (-)-Drimenol")
st.write("##### 中文名: 补身醇")
st.write("##### TPS original information: Phy_C15-TPS29_(-)-drimenol_14.085min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 14.085")
st.write("##### Formula: C15H26O")
st.write("##### Product proportion: 0.91")
st.write("##### Boiling Point: 298.8±9.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL32.png')
st.write("##### Mass spectrogram:")
st.image('image/LL32_MASS.png')
