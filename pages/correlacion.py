import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===== CARGAR DATOS ================================================
## Datos cargados desde app.py

# ===== ANÁLISIS DE DATOS ===========================================
df_tipo = df[['escarpado', 'monta_oso', 'ondulado', 
              'pavimento_asfaltico', 'pavimento_r_gido', 'pavimento_articulado']]

# ===== VISUALIZACIÓN DE DATOS ======================================
st.set_page_config(layout="centered")

st.title("Mapa de Correlación")
st.subheader("Correlación - Variables Numéricas")

## Mapa de Calor para Correlación
fig1, ax1 = plt.subplots()
sns.heatmap(df_tipo.corr(), annot=True, cmap='coolwarm', ax=ax1)
st.pyplot(fig1)
