from pathlib import Path
import pandas as pd
import streamlit as st

LOG_FILE = Path("logs.csv")


def load_logs():
    if LOG_FILE.exists():
        return pd.read_csv(
            LOG_FILE,
            header=None,
            names=["timestamp", "source_ip", "destination_ip", "alert_message"],
        )
    return pd.DataFrame(columns=["timestamp", "source_ip", "destination_ip", "alert_message"])


def main():
    st.set_page_config(page_title="IDS Dashboard", layout="wide")

    # --- Custom CSS (Cyber Theme) ---
    st.markdown("""
        <style>
        body {
            background-color: #0d1117;
            color: #e6edf3;
        }
        .stApp {
            background: linear-gradient(135deg, #0d1117, #111827);
        }
        h1, h2, h3 {
            color: #00ff9f;
        }
        .card {
            background-color: #161b22;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0,255,159,0.1);
            margin-bottom: 20px;
        }
        
        </style>
    """, unsafe_allow_html=True)

    # --- Header ---
    st.title("🛡️ Intrusion Detection System")
    st.caption("Real-time network monitoring dashboard")

    logs = load_logs()

    # --- Metrics Row ---
    col1, col2 = st.columns(2)
    col1.metric("📊 Total Logs", len(logs))
    alerts = logs[logs["alert_message"].str.contains("Possible scan", na=False)]
    col2.metric("🚨 Alerts", alerts["source_ip"].nunique())


    # --- Logs Section ---
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📡 Recent Network Logs")
    st.dataframe(logs.tail(20), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Alerts Section ---
    alerts = logs[logs["alert_message"].str.contains("Possible scan", na=False)]
    alerts = alerts.drop_duplicates(subset=["source_ip"])

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚨 Incidence Alerts")

    if alerts.empty:
        st.success("No threats detected ✅")
    else:
        st.markdown('<div class="alert-box">', unsafe_allow_html=True)
        st.dataframe(alerts.tail(20), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)



if __name__ == "__main__":
    main()
