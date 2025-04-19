
import streamlit as st
import pandas as pd
import os

st.title("Clasificador AFIP App")

uploaded_file = st.file_uploader("Subir archivo de compras AFIP", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Vista previa de los datos:")
    st.dataframe(df)

    for index, row in df.iterrows():
        proveedor = str(row.get("Proveedor", "Desconocido"))
        cuit = str(row.get("CUIT", "Sin CUIT"))

        st.write(f"**Proveedor:** {proveedor} ({cuit})")

        google_url = f"https://www.google.com/search?q={proveedor}+{cuit}"
        afip_url = f"https://www.afip.gob.ar/genericos/guiavirtual/consultas_detalle.aspx?id=218403"

        st.markdown(f"[Buscar en Google]({google_url})", unsafe_allow_html=True)
        st.markdown(f"[Buscar en AFIP]({afip_url})", unsafe_allow_html=True)

    output_path = os.path.join("outputs", "resultado.xlsx")
    df.to_excel(output_path, index=False)
    with open(output_path, "rb") as f_out:
        st.download_button("Descargar Excel Clasificado", f_out, file_name="resultado.xlsx")
    