#===========================================================
# LIBRERIRAS
#===========================================================
import streamlit as st
#===========================================================
# IMPORTS
#===========================================================
from datos.invitados import obtener_df_invitados
df_invitados=obtener_df_invitados()

#===========================================================
# PÁGINA
#===========================================================
st.title("Graduación del Edson🎓")

st.write(
    "Perros, en esta página podrán encontrar toda la información necesaria " \
    "respecto a mi gradución pro VIP MAX plus OMEGA remaster HD. Ubicaciones, instrucciones, " \
    "etc. Esto debido a que algunos de los invitados no pueden dejar de preguntar lo mismo " \
    "cada mes, ¿Se creen graciosos o qq?"
)


#columnas izquierda, centro derecha para alineacion de objetos
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.image("recursos/gifs/Amongus_GIF.gif",  use_container_width=True)

st.subheader("Invitados hasta el momento a la graduacion")
st.write(f"Hasta ahora hay {len(df_invitados)} invitados:")
st.dataframe(df_invitados, use_container_width=True, hide_index=True)