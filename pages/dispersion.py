import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===== CARGAR DATOS ================================================
url = 'data/datos_vias.csv'
df = pd.read_csv(url)
# ===== ANÁLISIS DE DATOS ===========================================
df_tipo = df[['escarpado', 'monta_oso', 'ondulado', 'plano', 'destapado',
              'afirmado', 'pavimento_asfaltico', 'pavimento_r_gido',
              'pavimento_articulado']]

columnas_numericas = df_tipo.columns.tolist()

# ===== VISUALIZACIÓN DE DATOS ======================================
st.set_page_config(layout="wide")

st.title("Gráfico de Dispersión")


col1, col2 = st.columns([1, 3])
with col1:
    var_x = st.selectbox("Variable eje X", columnas_numericas, index=0, key="scatter_x")
    var_y = st.selectbox("Variable eje Y", columnas_numericas, index=1, key="scatter_y")
with col2:
    fig, ax = plt.subplots()
    sns.scatterplot(data=df_tipo, x=var_x, y=var_y, ax=ax)
    ax.set_title(f'Gráfico de Dispersión: {var_x.capitalize()} vs {var_y.capitalize()}')
    st.pyplot(fig)
    plt.close(fig)

