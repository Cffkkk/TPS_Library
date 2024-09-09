import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL62")

st.write("##### CAS: [15423-57-1](https://scifinder-n.cas.org/searchDetail/substance/6560929525b43e48fcacc9a0/substanceDetails)")
st.write("##### Gene No: LT51")
st.write("##### Compounds Name: (1E,4E)-Germacrene B")
st.write("##### 中文名: 吉马烯B")
st.write("##### TPS original information: Pga_C15-TPS62_(1E,4E)-GermacreneB_9.915min_Standard")
st.write("##### Identification method in reference: Ref-Standard")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.915")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 287.2±40.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL62.png')
st.write("##### Mass spectrogram:")
st.image('image/LL62_MASS.png')
