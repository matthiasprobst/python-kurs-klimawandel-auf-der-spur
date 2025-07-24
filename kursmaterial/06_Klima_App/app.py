import streamlit as st


def compute_temperature(albedo):
    # Stefan-Boltzmann-Konstante in W/(m²·K⁴)
    sigma = 5.67e-8
    S = 1366

    # Berechnung der Temperatur in Kelvin
    T = ((1 - albedo) * S / (4 * sigma)) ** 0.25

    # Umrechnung in Grad Celsius
    T_celsius = T - 273.15
    return T_celsius


st.title("Klima App")

st.sidebar.header("Einstellungen")

albedo = st.sidebar.slider("Albedo", min_value=0.0, max_value=1.0, value=0.3)

temp = compute_temperature(albedo)
st.metric(label="Temperature basierend auf dem Albedo-Wert und der Solarkonstante [°C]", value=round(temp, 2))
