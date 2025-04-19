import streamlit as st
import pandas as pd
import json
import os
import urllib.parse

from utils import clasificar_comprobantes

# Cargar memoria
if os.path.exists("memory.json"):
    with open("memory.json", "r") as f:
        memory = json.load(f)
else:
    memory = {}

st.title("Clasificador de Compras AFIP")

uploaded_file = st.file_uploader("Subí un Excel de compras AFIP", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Vista previa del archivo:")
    st.dataframe(df.head())

    columnas = df.columns.tolist()
    cuit_col = st.selectbox("Seleccioná la columna de CUIT", columnas)
    proveedor_col = st.selectbox("Seleccioná la columna de Proveedor", columnas)

    if st.button("Clasificar Comprobantes"):
        df_clasificado = clasificar_comprobantes(df, cuit_col, proveedor_col, memory)
        output_path = "outputs/comprobantes_clasificados.xlsx"
        df_clasificado.to_excel(output_path, index=False)
        st.success(f"Archivo clasificado guardado en: {output_path}")
        st.write(df_clasificado)

        for index, row in df_clasificado.iterrows():
            proveedor = row[proveedor_col]
            cuit = row[cuit_col]
            google_url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(proveedor)
            afip_url = "https://www.afip.gob.ar/genericos/guiavirtual/consultas_detalle.aspx?id=3294415"

            st.markdown(f"**{proveedor}** (CUIT: {cuit})")
            st.markdown(f"[Buscar en Google]({google_url}) | [Buscar en AFIP]({afip_url})")
            st.write("---")

        with open("memory.json", "w") as f:
            json.dump(memory, f, indent=4)
