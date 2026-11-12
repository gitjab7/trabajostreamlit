import pandas as pd
import streamlit as st

aeropuertos =  pd.read_csv('ar-airports.csv')
st.title("Conozcamos nuestros datos")
st.header("🪪vamos a encontrar los datos principales del Dataset")
filas, columnas = aeropuertos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = aeropuertos.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
nombres_type = aeropuertos['type'].unique()
cant_type = len(aeropuertos['type'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna **type**?"):
    st.write(cant_type)
with st.expander("¿Cuáles son los valores únicos de la columna **type**?"):
    st.write(nombres_type)
with st.expander("¿Cuáles son los nombres de las columnas ?"):
   
    st.write(aeropuertos.columns)

        