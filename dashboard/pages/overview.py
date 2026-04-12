import streamlit as st
import pandas as pd

st.title("Overview")

if "scan_results" not in st.session_state:
    st.warning("Upload a file to see results.")
    st.stop()

df = pd.DataFrame(st.session_state["scan_results"])

st.metric("Total Vulnerabilities", len(df))

severity_counts = df["severity"].value_counts()

st.bar_chart(severity_counts)