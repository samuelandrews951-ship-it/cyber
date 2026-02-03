import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Real-Time Cyber Attack Map",
    layout="wide"
)

st.title("🌐 Real-Time Cyber-Attack Map")
st.write("Monitoring global cyber attacks in real time")

# -------------------- SIDEBAR --------------------
st.sidebar.header("Control Panel")
generate_attack = st.sidebar.button("Generate Attack")

# -------------------- SESSION STATE --------------------
if "attacks" not in st.session_state:
    st.session_state.attacks = pd.DataFrame(
        columns=["Time", "Attack Type", "Country", "Latitude", "Longitude", "Severity"]
    )

# -------------------- STATIC DATA --------------------
attack_types = ["DDoS", "Phishing", "Malware", "Ransomware", "Brute Force"]
severity_levels = ["Low", "Medium", "High", "Critical"]

country_locations = {
    "India": (20.5937, 78.9629),
    "USA": (37.0902, -95.7129),
    "UK": (55.3781, -3.4360),
    "Germany": (51.1657, 10.4515),
    "China": (35.8617, 104.1954),
    "Russia": (61.5240, 105.3188)
}

# -------------------- GENERATE ATTACK --------------------
if generate_attack:
    country = np.random.choice(list(country_locations.keys()))
    lat, lon = country_locations[country]

    new_attack = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Attack Type": np.random.choice(attack_types),
        "Country": country,
        "Latitude": lat + np.random.uniform(-1, 1),
        "Longitude": lon + np.random.uniform(-1, 1),
        "Severity": np.random.choice(severity_levels)
    }

    st.session_state.attacks = pd.concat(
        [st.session_state.attacks, pd.DataFrame([new_attack])],
        ignore_index=True
    )

# -------------------- LAYOUT --------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ Cyber Attack Map")
    if not st.session_state.attacks.empty:
        st.map(st.session_state.attacks[["Latitude", "Longitude"]])
    else:
        st.info("No cyber attacks detected")

with col2:
    st.subheader("📋 Recent Attacks")
    st.dataframe(
        st.session_state.attacks.tail(10),
        use_container_width=True
    )

# -------------------- ALERT SYSTEM --------------------
if not st.session_state.attacks.empty:
    severity = st.session_state.attacks.iloc[-1]["Severity"]

    if severity == "Critical":
        st.error("🚨 Critical Cyber Attack Detected")
    elif severity == "High":
        st.warning("⚠️ High Severity Cyber Attack Detected")
