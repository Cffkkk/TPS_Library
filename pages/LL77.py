import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL77")

st.write("##### CAS: [502-61-4](https://scifinder-n.cas.org/searchDetail/substance/65640658aa727207d5700201/substanceDetails)")
st.write("##### Gene No: LT62")
st.write("##### Compounds Name: α-Farnesene ")
st.write("##### 中文名: α-金合欢烯")
st.write("##### TPS original information: Mdo_AFS_α-farnesene_10.79min_NMR")
st.write("##### Identification method in reference: Ref-NMR")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 10.79")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 125 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL77.png')
st.write("##### Mass spectrogram:")
st.image('image/LL77_MASS.png')
