#Mapas
import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


aeropuertos = pd.read_csv('ar-airports.csv')
st.title("🗺️Distribucion de los tipos de Aeropuertos mostrados en un mapa")
mapa = generar_mapa()

def agregar_marca_aerop(row):
    
    folium.Marker(
        [row['latitude_deg'], row['longitude_deg']],
        popup=row['name'],
        icon=folium.Icon()
        
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])

r_areas = ac1.checkbox("Grandes")

if r_areas:
    a_larg = aeropuertos[aeropuertos['type']=='large_airport']
    a_larg.apply(agregar_marca_aerop, axis=1)
r_parques = ac1.checkbox("Medianos")
if r_parques:
    a_med = aeropuertos[aeropuertos['type']=='medium_airport']
    a_med.apply(agregar_marca_aerop, axis=1)
r_monu = ac1.checkbox("Pequeños")
if r_monu:
    a_small = aeropuertos[aeropuertos['type']=='small_airport']
    a_small.apply(agregar_marca_aerop, axis=1)
r_closed = ac1.checkbox("Cerrados")
if r_closed:
    a_closed = aeropuertos[aeropuertos['type']=='closed']
    a_closed.apply(agregar_marca_aerop, axis=1)
r_helipuerto = ac1.checkbox("Helipuertos")
if r_helipuerto:
    a_helipuerto = aeropuertos[aeropuertos['type']=='heliport']
    a_helipuerto.apply(agregar_marca_aerop, axis=1)
r_balloon = ac1.checkbox("Globos Aerostaticos")
if r_balloon:
    a_balloon = aeropuertos[aeropuertos['type']=='balloonport']
    a_balloon.apply(agregar_marca_aerop, axis=1) 

with ac2:
    st_folium(mapa, key='aeropuertos')