import streamlit as st
import pandas as pd
import joblib

# Cargar modelo entrenado
modelo = joblib.load("modelo_rul.pkl")

# Título
st.title("🔧 Predicción de Vida Útil (RUL)")
st.subheader("Motores Eléctricos Industriales")

# Entradas del usuario
horas = st.slider("Horas de operación", 0, 10000, 5000)
temperatura = st.slider("Temperatura (°C)", 40, 100, 70)
vibracion = st.slider("Vibración (mm/s)", 1, 10, 5)

# Botón de predicción
if st.button("Predecir RUL"):

    entrada = pd.DataFrame({
        "Horas": [horas],
        "Temperatura": [temperatura],
        "Vibracion": [vibracion]
    })

    prediccion = modelo.predict(entrada)[0]

    st.success(f"Vida útil estimada: {round(prediccion)} horas")

    porcentaje = max(0, min(100, prediccion / 20000 * 100))
    st.progress(int(porcentaje))

    if prediccion >= 14000:
        st.success("🟢 Estado: Bueno")
    elif prediccion >= 9000:
        st.warning("🟡 Estado: Medio")
    else:
        st.error("🔴 Estado: Crítico")

    st.write("### Datos ingresados")
    st.write(f"Horas de operación: {horas}")
    st.write(f"Temperatura: {temperatura} °C")
    st.write(f"Vibración: {vibracion} mm/s")