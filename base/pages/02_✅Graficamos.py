import streamlit as st
import pandas as pd
import plotly.express as px

aeropuertos = pd.read_csv('ar-airports.csv')

# Gráfico de barras
st.title("📊Graficámos con el Dataset")

filtro = aeropuertos['region_name'].value_counts().reset_index()
filtro.columns = ['Provincia', 'Cantidad']

fig = px.bar(
    filtro,
    x='Cantidad',
    y='Provincia',
    title="Cantidad de Aeropuertos por Provincia"
)

st.plotly_chart(fig)


# Gráfico de torta
st.title("Gráfico de torta")

filtro = aeropuertos['type'].value_counts().reset_index()
filtro.columns = ['Tipo', 'Cantidad']

fig = px.pie(
    filtro,
    names='Tipo',
    values='Cantidad',
    title="Porcentajes de tipos de Aeropuertos"
)

st.plotly_chart(fig)
