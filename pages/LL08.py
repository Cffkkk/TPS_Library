import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL08")

st.write("##### CAS: [507-70-0](https://scifinder-n.cas.org/searchDetail/substance/6560636d25b43e48fca91808/substanceDetails)")
st.write("##### Gene No: LT08")
st.write("##### Compounds Name: Boreneol")
st.write("##### 中文名: 冰片/龙脑")
st.write("##### TPS original information: Wvi_C10-TPS27_boreneol_6.460min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 6.46")
st.write("##### Formula: C10H18O")
st.write("##### Product proportion: 0.03999882")
st.write("##### Boiling Point: 213.2 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL08.png')
st.write("##### Mass spectrogram:")
st.image('image/LL08_MASS.png')
