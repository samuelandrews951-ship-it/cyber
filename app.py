import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page config
st.set_page_config(page_title="Real-Time Cyber Attack Map", layout="wide")

st.title("🌐 Real-Time Cyber-Attack Monitoring Map")
st.write("Visualizing live cyber attacks across the globe")

# Sidebar
st.sidebar.header("⚙️ Control Panel")
generate = st.sidebar.button("🚨 Generate Cyber Attack")

# Initialize session state
if "attack_data" not in st.session_state:
    st.session_state.attack_data = pd.DataFrame(
        columns=[
            "Time", "Attack Type", "Country",
            "Latitude", "Longitude", "Severity"
        ]
    )

# Sample attack data
attack_types = ["DDoS", "Phishing", "Malware", "Ransomware", "Brute Force"]
countries = {
    "USA": [37.0902, -95.7129],
    "India": [20.5937, 78.9629],
    "China": [35.8617, 104.1954],
    "Russia": [61.5240, 105.3188],
    "Germany": [51.1657, 10.4515],
    "UK": [55.3781, -3.4360]
}
severities = ["Low", "Medium", "High", "Critical"]

# Generate attack
if generate:
    country = np.random.choice(list(countries.keys()))
    lat, lon = countries[country]

    new_attack = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Attack Type": np.random.choice(attack_types),
        "Country": country,
        "Latitude": lat + np.random.uniform(-1, 1),
        "Longitude": lon + np.random.uniform(-1, 1),
        "Severity": np.random.choice(severities)
    }

    st.session_state.attack_data = pd.concat(
        [st.session_state.attack_data, pd.DataFrame([new_attack])],
        ignore_index=True
    )

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ Live Cyber Attack Map")
    if not st.session_state.attack_data.empty:
        st.map(
            st.session_state.attack_data[["Latitude", "Longitude"]]
        )
    else:
        st.info("No attacks detected yet")

with col2:
    st.subheader("📊 Recent Attacks")
    st.dataframe(st.session_state.attack_data.tail(10), use_container_width=True)

# Severity alert
if not st.session_state.attack_data.empty:
    last_severity = st.session_state.attack_data.iloc[-1]["Severity"]
    if last_severity == "Critical":
        st.error("🚨 Critical Cyber Attack Detected!")
    elif last_severity == "High":
        st.warning("⚠️ High Severity Cyber Attack Detected!")
