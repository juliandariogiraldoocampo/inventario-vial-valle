import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===== ENCABEZADO ==================================================
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


st.image('img/inventario_vial.png', use_container_width=True)
st.subheader("Una mirada a la infraestructura vial del departamento")

st.write("""
Esta aplicacion explora el **Inventario Vial Departamental** del Valle del Cauca, publicado en el portal nacional de datos abiertos. 
         
El dataset describe, para cada tramo de via:
""")

st.markdown("- **Longitud**")
st.markdown("- **Tipo de terreno**")
st.markdown("- **Tipo de superficie**")
st.markdown("- **Estado de conservacion**")

st.divider()

st.subheader("Que puedes hacer aqui")

st.write("Usa el **menu lateral** para navegar entre los analisis:")

col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.markdown("**Inicio**")
        st.caption("Vision general e indicadores clave")
with col2:
    with st.container(border=True):
        st.markdown("**Categorias**")
        st.caption("Longitud por categoria de via y municipio")
with col3:
    with st.container(border=True):
        st.markdown("**Municipios**")
        st.caption("Estado de las vias por municipio")

st.divider()

st.subheader("Por que es importante")

st.warning("Contar con datos de infraestructura disponibles, actualizados y accesibles es clave para el analisis territorial y la planeacion del desarrollo.")

st.write("Los datos viales permiten:")

st.markdown("- Identificar tramos criticos")
st.markdown("- Priorizar inversiones en mantenimiento")
st.markdown("- Planificar rutas logisticas y movilidad")
st.markdown("- Apoyar decisiones publicas con evidencia")

st.divider()

st.subheader("Fuente de los datos")
st.link_button("Datos abiertos del gobierno colombiano", "https://www.datos.gov.co/Transporte/Inventario-Vial-Departamental/tsgc-irwm/about_data")