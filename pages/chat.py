#=======================================
# LIBRERIAS
#======================================
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

#=====================================
# IMPORTS
#=======================================
from datos.datos_chat import (
    guardar_comentario,
    obtener_comentarios
)

#============================================
#interfaz del chat
#============================================
st.title("💬 Chat de la graduación")
st.write("Aqui pueden dejar sus comentarios, opiniones o cualquier " \
    "madre que quieran escribir."
)

alias = st.session_state.get("alias")

if not alias:
    st.warning("Debes iniciar sesión para acceder al chat.")
    st.stop()

with st.form("form_comentario", clear_on_submit=True):
    mensaje = st.text_area(
        "Escribe tu comentario",
        max_chars=1000
    )
    publicar = st.form_submit_button("Publicar")

if publicar:
    mensaje = mensaje.strip()

    if not mensaje:
        st.warning("Escribe un comentario primero.")
    else:
        try:
            guardar_comentario(alias, mensaje)
            st.success("¡Comentario publicado!")
            st.rerun()
        except Exception:
            st.error("No se pudo publicar el comentario.")

st.divider()
st.subheader("Comentarios de los invitados")


@st.fragment(run_every="5s")
def mostrar_comentarios():
    try:
        comentarios = obtener_comentarios()
    except Exception:
        st.error("No se pudieron cargar los comentarios.")
        return

    if not comentarios:
        st.info("Todavía no hay comentarios.")
        return

    for c in comentarios:
        with st.chat_message("user", avatar="🎓"):
            st.markdown(f"**{c['alias']}**")

            fecha = datetime.fromisoformat(
                c["fecha"].replace("Z", "+00:00")
            ).astimezone(ZoneInfo("America/Monterrey"))

            st.caption(fecha.strftime("%d/%m/%Y %H:%M"))
            st.write(c["mensaje"])


mostrar_comentarios()
