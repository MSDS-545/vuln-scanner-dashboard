import streamlit as st
import pandas as pd

st.title("Scan Results")

if "scan_results" not in st.session_state:
    st.warning("No scan results available.")
    st.stop()

df = pd.DataFrame(st.session_state["scan_results"])

st.dataframe(df)