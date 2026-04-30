import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🔐 Vulnerability Overview")
st.caption("Summary of detected security issues in your uploaded file.")
st.divider()

if "scan_results" not in st.session_state:
    st.warning("⚠️ Upload a file to see results.")
    st.stop()

df = pd.DataFrame(st.session_state["scan_results"])

# ── Metric cards ──────────────────────────────────────
severity_counts = df["severity"].value_counts()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("🔎 Total",    len(df))
col2.metric("🔴 Critical", severity_counts.get("CRITICAL", 0))
col3.metric("🟠 High",     severity_counts.get("HIGH",     0))
col4.metric("🟡 Medium",   severity_counts.get("MEDIUM",   0))
col5.metric("🟢 Low",      severity_counts.get("LOW",      0))

st.divider()

# ── Severity bar chart ────────────────────────────────
st.subheader("Severity Breakdown")

severity_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
ordered_counts = severity_counts.reindex(severity_order).fillna(0)
st.bar_chart(ordered_counts, use_container_width=True, height=300)

st.divider()

# ── Raw results table ─────────────────────────────────
st.subheader("Detected Issues")
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

# ── Status alert ──────────────────────────────────────
critical = severity_counts.get("CRITICAL", 0)
high     = severity_counts.get("HIGH",     0)

if critical > 0:
    st.error(f"🔴 {critical} critical issue(s) found — fix immediately.")
elif high > 0:
    st.warning(f"🟠 {high} high-severity issue(s) found — review soon.")
else:
    st.success("✅ No critical or high vulnerabilities detected.")