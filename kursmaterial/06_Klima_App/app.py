import streamlit as st


def compute_temperature(albedo):
    return 0.0

st.title("Klima App")
st.write("This is a simple Streamlit app to demonstrate the Klima App functionality.")

st.sidebar.header("Settings")
st.sidebar.write("Adjust the settings below to customize the app.")

albedo = st.sidebar.slider("Albedo", min_value=0.0, max_value=1.0, value=0.3)
st.write("You can add more functionality here, such as data visualization, climate statistics, etc.")

st.metric(label="Temperature based on albedo", value=f"{compute_temperature(albedo):.2f} °C",)
