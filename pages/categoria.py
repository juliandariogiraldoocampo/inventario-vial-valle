import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Longitud (km) por Categoría")

# === CARGAR DATOS ==================================================
## Datos cargados desde app.py


# === ANALISIS DE DATOS =============================================
categoria = st.selectbox("Selecciona una categoría", df['categor_a'].sort_values().unique())
df_filtrado = df[df['categor_a'] == categoria]
df_filtrado = df_filtrado.sort_values('longitud_km', ascending=False)

# === VISUALIZACION DE DATOS ========================================
fig, ax = plt.subplots(figsize=(12, max(3, len(df_filtrado) * 0.35)))
sns.barplot(data=df_filtrado, x='longitud_km', y='municipios', errorbar=None, ax=ax)
ax.set_title(f'Longitud (km) - Categoría: {categoria}')
st.pyplot(fig)
plt.close(fig)