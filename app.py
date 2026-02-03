import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Real-Time Cyber Attack Map", layout="wide")

st.title("🛡️ Real-Time Cyber-Attack Map")
st.write("Live visualization of global cyber attack activities")

# Sidebar controls
st.sidebar.header("⚙️ Control Panel")
generate = st.sidebar.button("🔄 Generate Attack Event")

# Initialize session state
if "attack_data" not in st.session_state:
    st.session_state.attack_data = pd.DataFrame(
        columns=["Time", "Latitude", "Longitude", "Attack Type", "Severity"]
    )

# Attack types
attack_types = ["DDoS", "Phishing", "Malware", "Ransomware", "Brute Force"]
severity_levels = ["Low", "Medium", "High"]

# Generate attack data
def generate_attack():
    return {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Latitude": np.random.uniform(-60, 60),
        "Longitude": np.random.uniform(-180, 180),
        "Attack Type": np.random.choice(attack_types),
        "Severity": np.random.choice(severity_levels)
    }

# Generate new attack event
if generate:
    new_attack = generate_attack()
    st.session_state.attack_data = pd.concat(
        [st.session_state.attack_data, pd.DataFrame([new_attack])],
        ignore_index=True
    )

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("🌐 Total Attacks", len(st.session_state.attack_data))
col2.metric("⚠️ High Severity",
            len(st.session_state.attack_data[
                st.session_state.attack_data["Severity"] == "High"
            ]))
col3.metric("🕒 Last Update",
            st.session_state.attack_data["Time"].iloc[-1]
            if len(st.session_state.attack_data) > 0 else "N/A")

# Map visualization
st.subheader("🌍 Global Cyber Attack Map")
if len(st.session_state.attack_data) > 0:
    st.map(st.session_state.attack_data[["Latitude", "Longitude"]])
else:
    st.info("Click 'Generate Attack Event' to start")

# Attack log
st.subheader("📄 Attack Event Log")
st.dataframe(st.session_state.attack_data)
