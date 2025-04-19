
import streamlit as st
import pandas as pd

st.title("Clasificador AFIP App")
st.write("Subí tu archivo Excel para clasificar comprobantes.")

uploaded_file = st.file_uploader("Seleccioná un archivo Excel", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
