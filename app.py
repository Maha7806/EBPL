
import streamlit as st
import pandas as pd

import numpy as np
import time
import datetime
import plotly.express as px

st.set_page_config(page_title="Smart Building Health Dashboard", layout="wide")
st.title("Smart Building Health Dashboard")
st.markdown("Monitor the structural health of a building using real-time simulated or uploaded sensor data.")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a CSV File", type=["csv"])

# Initialize session state
if "sensor_data" not in st.session_state:
    st.session_state.sensor_data = pd.DataFrame(columns=["timestamp", "vibration", "temperature", "strain", "humidity"])

# Try loading uploaded CSV
if uploaded_file is not None:
    try:
        df_uploaded = pd.read_csv(uploaded_file, parse_dates=["timestamp"])
        st.session_state.sensor_data = df_uploaded
        st.success("CSV file loaded successfully!")
    except Exception as e:
        st.error(f"Failed to read CSV: {e}")

# Simulation function
def simulate_sensors():
    return {
        "timestamp": datetime.datetime.now(),
        "vibration": round(np.random.normal(3, 1), 2),
        "temperature": round(np.random.normal(25, 2), 2),
        "strain": round(np.random.normal(5, 0.5), 2),
        "humidity": round(np.random.normal(50, 5), 2),
    }

# Sidebar controls
update_interval = st.sidebar.slider("Update Interval (seconds)", 1, 10, 2)
run_monitoring = st.sidebar.checkbox("Start Real-Time Monitoring")
save_csv = st.sidebar.button("Download Current Data as CSV")

# Metrics display
col1, col2, col3, col4 = st.columns(4)
placeholder = st.empty()

# Monitoring loop
if run_monitoring and uploaded_file is None:
    while True:
        new_data = simulate_sensors()
        st.session_state.sensor_data = pd.concat([
            st.session_state.sensor_data,
            pd.DataFrame([new_data])
        ], ignore_index=True)

        col1.metric("Vibration (mm/s)", new_data["vibration"])
        col2.metric("Temperature (°C)", new_data["temperature"])
        col3.metric("Strain (μɛ)", new_data["strain"])
        col4.metric("Humidity (%)", new_data["humidity"])

        # Alerts
        if new_data["vibration"] > 6:
            st.error("High Vibration Detected!")
        if new_data["temperature"] > 30:
            st.warning("High Temperature!")
        if new_data["strain"] > 6:
            st.warning("Structural Strain Exceeding Normal Range!")

        # Chart
        with placeholder.container():
            df = st.session_state.sensor_data.tail(50)
            fig = px.line(df, x="timestamp", y=["vibration", "temperature", "strain", "humidity"],
                          labels={"value": "Sensor Value", "timestamp": "Time"},
                          title="Sensor Trends Over Time")
            st.plotly_chart(fig, use_container_width=True)

        time.sleep(update_interval)
        st.rerun()

# Download CSV
if save_csv:
    csv = st.session_state.sensor_data.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(" Download CSV", data=csv, file_name="sensor_data.csv", mime="text/csv")

# Show uploaded data if monitoring is off
if not run_monitoring and not st.session_state.sensor_data.empty:
    st.subheader("Uploaded or Simulated Sensor Data Preview")
    st.dataframe(st.session_state.sensor_data.tail(20))
