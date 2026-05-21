import streamlit as st
import pandas as pd
import os

url = 'data/datos_vias.csv'
df = pd.read_csv(url)

pg = st.navigation([
    st.Page("pages/inicio.py", title="Inicio", default=True),
    st.Page("pages/dispersion.py", title="Grafico de Dispersion"),
    st.Page("pages/categoria.py", title="Longitud por Categoria y Municipio"),
    st.Page("pages/estado.py", title="Comparación de Estado por Municipio"),
    st.Page("pages/correlacion.py", title="Mapa de Correlacion")
])
pg.run()

with st.sidebar:
    zip_path = "proyecto.zip"

    if os.path.exists(zip_path):
        with open(zip_path, "rb") as f:
            st.download_button(
                label="📥 Descargar .zip del Proyecto",
                data=f,
                file_name="proyecto.zip",
                mime="application/zip"
            )
    else:
        st.error(f"❌ No se encontró el archivo '{zip_path}' en la raíz del proyecto.")