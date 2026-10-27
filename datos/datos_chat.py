#=====================================
# LIBRERIAS
#=====================================
import streamlit as st
from supabase import create_client


#=================================================
# FUNCIONES PARA GUARDAR Y OCULTAR MENSAJES
#=================================================
@st.cache_resource
def obtener_conexion():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


def guardar_comentario(alias, mensaje):
    return (
        obtener_conexion()
        .table("comentarios")
        .insert({
            "alias": alias,
            "mensaje": mensaje
        })
        .execute()
    )


def obtener_comentarios():
    respuesta = (
        obtener_conexion()
        .table("comentarios")
        .select("id, alias, mensaje, fecha")
        .order("fecha", desc=True)
        .limit(100)
        .execute()
    )

    return respuesta.data