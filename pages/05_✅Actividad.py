import streamlit as st

st.set_page_config(page_title="Actividad", page_icon="🎮")
st.title("🎮 Preguntas multiple choice para terminar")

# ============================================================
# Definimos las preguntas
# ============================================================
preguntas = [
    {
        "pregunta": "Cuantas filas y columnas tiene el dataset?",
        "opciones": ["67 x 67", "956 x 24", "1024 x 574"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cual es el tipo de aeropuerto de mayor porcentaje?",
        "opciones": ["Balloonport", "Large_Airport", "Small_airport"],
        "correcta": 2
    },
    {
        "pregunta": "¿En que provincia estan ubicados mas aeropuertos?",
        "opciones": ["Buenos Aires", "Mendoza", "Chacarita"],
        "correcta": 0
    },
]

# ============================================================
# Una pregunta por bloque, con su propio botón de verificar
# ============================================================
for i, p in enumerate(preguntas):
    st.subheader(f"Pregunta {i + 1}")
    st.write(p["pregunta"])

    # El radio guarda la elección del estudiante
    eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    # Cada pregunta tiene su propio botón
    if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.balloons()
            st.success("✅ ¡Correcto!")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"❌ Incorrecto. La respuesta correcta era: **{correcta}**")

    st.divider()