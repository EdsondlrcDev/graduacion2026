# =========================================================
# LIBRERÍAS
# =========================================================
import time

import streamlit as st


# ========================================================
# IMPORTS
# ========================================================
from datos.UsuariosContrasenas import usuarios


# ============================================================
# LOGIN
# ============================================================
def mostrar_login():
    st.title("🎓 Graduación 2026")
    st.subheader("Iniciar sesión")

    mensaje_login = st.session_state.pop("mensaje_login", None)
    if mensaje_login:
        st.warning(mensaje_login)

    with st.form("formulario_login"):
        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        enviar = st.form_submit_button("Entrar", use_container_width=True)

    if enviar:
        with st.status("Preparando la autenticación...", expanded=False) as estado_login:
            # La validación local es prácticamente instantánea. Esta pausa breve
            # permite que el usuario vea el estado antes de la redirección.
            time.sleep(0.8)

            # El usuario no distingue mayúsculas y minúsculas; la contraseña sí.
            usuario_busqueda = usuario.strip().casefold()
            usuario_encontrado = next(
                (
                    nombre_usuario
                    for nombre_usuario in usuarios
                    if nombre_usuario.casefold() == usuario_busqueda
                ),
                None,
            )

            credenciales_validas = (
                usuario_encontrado is not None
                and usuarios[usuario_encontrado]["contraseña"] == password
            )

            if credenciales_validas:
                datos_usuario = usuarios[usuario_encontrado]
                st.session_state.usuario = usuario_encontrado
                st.session_state.alias = datos_usuario["alias"]
                st.session_state.ultima_actividad = time.time()
                st.session_state.redirigir_inicio = True
                estado_login.update(
                    label="Autenticación correcta. Redirigiendo...",
                    state="complete",
                )
                time.sleep(0.4)
                st.rerun()

            estado_login.update(
                label="No se pudo completar la autenticación.",
                state="error",
            )

        st.error("Usuario o contraseña incorrectos")


mostrar_login()
