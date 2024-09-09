import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL104")

st.write("##### CAS: [22469-52-9](https://scifinder-n.cas.org/searchDetail/substance/656806a8aa727207d5b784c7/substanceDetails)")
st.write("##### Gene No: LT83")
st.write("##### Compounds Name: (+)-Cyclosativene")
st.write("##### 中文名: (+)-环苜蓿烯")
st.write("##### TPS original information: V5-7_(+)-Cyclosativene_9.185min_NIST")
st.write("##### Identification method in reference: NIST")
st.write("##### Main product or by-product: By-product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 9.185")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: No information")
st.write("##### Boiling Point: 243.4±7.0 °C (predicted)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL104.png')
st.write("##### Mass spectrogram:")
st.image('image/LL104_MASS.png')
