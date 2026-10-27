#===========================================================
# LIBRERIRAS
#===========================================================
import streamlit as st
import folium
from streamlit_folium import st_folium 
#===========================================================
# IMPORTS
#===========================================================
from datos.ubicaciones import ubicaciones

#===========================================================
# PROCESOS
#===========================================================
st.title("Graduación: 05/dic/2026")
st.write("podran ver toda la información necesaria para prepararse el día de la graduación.")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("recursos/gifs/TRALALERO_GIF.gif")

#Ubicacion
st.subheader("Ubicación del salón")
st.write("El salón se llama 'Panorama', está en Carr. Nacional 500-Loc C301, Valle Alto, 64983 Monterrey, N.L. " \
"A unos 35 minutos del centro de Monterrey. " \
"Hay que venir bien vestidos y por favor, bañense (Alejandra), les paso una ubicación más precisa " \
"junto a otras ubicaciones de reelevancia. ")

# Crear mapa centrado en la primera ubicación
mapa = folium.Map(
    location=ubicaciones[0]["coords"],
    zoom_start=14
)

# Agregar todos los marcadores
for lugar in ubicaciones:
    folium.Marker(
        location=lugar["coords"],
        tooltip=lugar["nombre"],
        popup=lugar["descripcion"],
        icon=folium.Icon(color=lugar["color"])
    ).add_to(mapa)

# Mostrar en Streamlit
st_folium(mapa, use_container_width=True, height=500)

#info del hotel
st.subheader("Hotel (ubicación en el mapa de arriba, solo alejen el zoom)")
st.write("El grupo de planeación de graduación tiene un convenio con un hotel cercano (18 minutos en carro aprox al salón) " \
"con tarifas preferenciales para cada tipo de habitación, les paso la info con detalles para hacer la reserva, " \
"no es obligatoria hacerla en ese hotel, solo es la opción que nos han facilitado a alumnos y arrimados.")

st.image("recursos/imagenes/INFO_HOTEL.png",  use_container_width=True)