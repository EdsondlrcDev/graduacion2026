# ===========================================================
# LIBRERÍAS
# ===========================================================
import time

import streamlit as st


# ===========================================================
# CONFIGURACIÓN GENERAL
# ===========================================================
TIEMPO_MAXIMO_INACTIVIDAD = 15 * 60

st.set_page_config(
    page_title="Graduación 2026",
    page_icon="🎓",
    initial_sidebar_state="collapsed",
)


# ===========================================================
# CONTROL DE SESIÓN
# ===========================================================
def inicializar_sesion():
    """Crea las variables de sesión necesarias para la autenticación."""
    valores_iniciales = {
        "usuario": None,
        "alias": None,
        "ultima_actividad": None,
        "redirigir_inicio": False,
    }

    for clave, valor in valores_iniciales.items():
        if clave not in st.session_state:
            st.session_state[clave] = valor


def cerrar_sesion():
    """Elimina los datos de autenticación de la sesión actual."""
    st.session_state.usuario = None
    st.session_state.alias = None
    st.session_state.ultima_actividad = None
    st.session_state.redirigir_inicio = False


def verificar_sesion():
    """Expira la sesión después de 15 minutos sin una nueva interacción."""
    if st.session_state.usuario is None:
        return

    ultima_actividad = st.session_state.ultima_actividad
    tiempo_actual = time.time()

    if (
        ultima_actividad is None
        or tiempo_actual - ultima_actividad >= TIEMPO_MAXIMO_INACTIVIDAD
    ):
        cerrar_sesion()
        st.session_state.mensaje_login = (
            "Tu sesión expiró después de 15 minutos de inactividad. "
            "Inicia sesión nuevamente."
        )
        st.rerun()

    # Cada ejecución provocada por una interacción renueva la actividad.
    st.session_state.ultima_actividad = tiempo_actual


inicializar_sesion()
verificar_sesion()


# ===========================================================
# LOGIN: NO SE MUESTRA NINGUNA PÁGINA HASTA AUTENTICARSE
# ===========================================================
if st.session_state.usuario is None:
    navegacion_login = st.navigation(
        [
            st.Page(
                "auth/login.py",
                title="Iniciar sesión",
                icon="🔐",
            )
        ],
        position="hidden",
    )
    navegacion_login.run()
    st.stop()


# ===========================================================
# NAVEGACIÓN PROTEGIDA Y SIDEBAR
# ===========================================================
paginas = [
    st.Page("pages/inicio.py", title="Inicio", icon="🏠"),
    st.Page("pages/Informacion_graduacion.py",title="Información",icon="📅",),
    st.Page("pages/chat.py",title="Chat de invitados",icon="💬"),
]


navegacion = st.navigation(paginas, position="sidebar")

with st.sidebar:
    st.write(f"👤 {st.session_state.alias}")

    if st.button("Cerrar sesión", use_container_width=True):
        cerrar_sesion()
        st.rerun()


# El primer destino después de autenticarse siempre es Inicio.
if st.session_state.redirigir_inicio:
    st.session_state.redirigir_inicio = False
    st.switch_page("pages/inicio.py")

navegacion.run()
