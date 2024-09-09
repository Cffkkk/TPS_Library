import streamlit as st
# st.set_page_config(layout="wide")
st.title("LL68")

st.write("##### CAS: [515-17-3](https://scifinder-n.cas.org/searchDetail/substance/656404f9aa727207d56fe375/substanceDetails)")
st.write("##### Gene No: LT54")
st.write("##### Compounds Name: Selina-4(15),7(11)-diene")
st.write("##### 中文名: No information")
st.write("##### TPS original information: Spr_C15-TPS65_Selina-4(15),7(11)-diene_11.350min")
st.write("##### Identification method in reference: No information")
st.write("##### Main product or by-product: Main product")
st.write("##### Detecting instrument model: GCMS-TQ8040 NX")
st.write("##### RT min: 11.35")
st.write("##### Formula: C15H24")
st.write("##### Product proportion: 0.95")
st.write("##### Boiling Point: 128-133 °C (exprimental)")
col1, col2 = st.columns([1,6])
with col1:
    st.write("##### Structure: ")
with col2:
    st.image('image/LL68.png')
st.write("##### Mass spectrogram:")
st.image('image/LL68_MASS.png')
