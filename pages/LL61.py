import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL61")

st.write("##### CAS: [473-13-2](https://scifinder-n.cas.org/searchDetail/substance/6560924b25b43e48fcacc502/substanceDetails)")
st.write("##### Gene No: LT50")
st.write("##### Compounds Name: α-Selinene")
st.write("##### 中文名: α-芹子烯")
st.write("##### TPS original information: Zma_C15-TPS61_α-Selinene_10.850min__Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.85")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 135 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL61.png')
st.write("##### Mass spectrogram:")
st.image('image/LL61_MASS.png')
