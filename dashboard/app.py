import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/scan"

st.set_page_config(page_title="Vulnerability Scanner Dashboard")

st.title("Code Vulnerability Scanner")

uploaded_file = st.file_uploader("Upload Python File", type=["py"])

if uploaded_file:

    response = requests.post(
        API_URL,
        files={"file": (uploaded_file.name, uploaded_file.getvalue())}
    )

    data = response.json()

    issues = data.get("issues", [])

    st.session_state["scan_results"] = issues

    st.success(f"Scan complete. {len(issues)} vulnerabilities found.")

    df = pd.DataFrame(issues)

    st.dataframe(df)