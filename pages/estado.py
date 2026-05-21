import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==== CARGAR DATOS ==================================================
## Datos cargados desde app.py

# ==== ANALISIS DE DATOS =================================================

listado_municipios = df['municipios'].unique()

# === CONFIGURACION DE PAGINA =========================================
st.set_page_config(layout="wide")
st.title("Estado de la Vía por Municipio")

# === VISUALIZACION DE DATOS =============================================
municipios = st.multiselect(
    "Selecciona uno o varios municipios",
    listado_municipios,
    default=listado_municipios[:3]
)

df_filtrado = df[df['municipios'].isin(municipios)]
estado = df_filtrado[['municipios', 'bueno', 'regular', 'malo', 'p_simo']]

estado_largo = estado.melt(id_vars='municipios', var_name='Estado', value_name='Longitud')

fig, ax = plt.subplots(figsize=(12, max(3, len(estado_largo) * 0.15)))
sns.barplot(data=estado_largo, x='Longitud', y='municipios', hue='Estado', errorbar=None, ax=ax)
ax.set_title('Estado de la vía por municipio')
#plt.xticks(rotation=45)
st.pyplot(fig)
plt.close(fig) 
