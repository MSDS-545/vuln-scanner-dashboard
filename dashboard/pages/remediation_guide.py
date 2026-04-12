import streamlit as st
import pandas as pd

st.title("Remediation Guide")

if "scan_results" not in st.session_state:
    st.warning("Run a scan first.")
    st.stop()

df = pd.DataFrame(st.session_state["scan_results"])

for _, row in df.iterrows():

    st.subheader(row["type"])

    st.write(f"Severity: {row['severity']}")

    if row["type"] == "unsafe function":
        st.write("Avoid using eval() or exec().")

    elif row["type"] == "SQL injection risk":
        st.write("Use parameterized queries.")

    elif row["type"] == "unvalidated input":
        st.write("Validate user input before processing.")

    else:
        st.write("Follow OWASP secure coding practices.")