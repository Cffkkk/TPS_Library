import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL19")

st.write("##### CAS: [13474-59-4](https://scifinder-n.cas.org/searchDetail/substance/6560694c25b43e48fca9a509/substanceDetails)")
st.write("##### Gene No: LT17")
st.write("##### Compounds Name: (E)-α-Bergamotene")
st.write("##### 中文名: 香柑油烯/佛手柑油烯")
st.write("##### TPS original information: Lan_C15-TPS12_(E)-a-Bergamotene_9.975min_NIST")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.975")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.67")
st.write("##### Boiling Point: 259.5±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL19.png')
st.write("##### Mass spectrogram:")
st.image('image/LL19_MASS.png')
