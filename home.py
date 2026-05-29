import streamlit as st
import plotly.express as px

from utils.loader_scope import load_scope
from utils.loader_relied import load_relied
from utils.risk_engine import calculate_risk, risk_level
from utils.text_utils import detect_change


def render_home():

    # ---------------------------
    # LOAD DATA
    # ---------------------------
    df = load_scope()
    relied_df = load_relied()

    # ---------------------------
    # SAFETY CHECKS (VERY IMPORTANT)
    # ---------------------------
    # Prevent crashes if column missing
    if "full_text" not in df.columns:
        df["full_text"] = ""

    if "supplier" not in relied_df.columns:
        relied_df["supplier"] = False

    # ---------------------------
    # AI PROCESSING
    # ---------------------------
    df["risk_score"] = df["full_text"].apply(calculate_risk)
    df["risk_level"] = df["risk_score"].apply(risk_level)
    df["change_flag"] = df["full_text"].apply(detect_change)

    # ---------------------------
    # FILTERING
    # ---------------------------
    phase = st.session_state.get("phase", "All")
    discipline = st.session_state.get("discipline", "All")

    if phase != "All" and "phase" in df.columns:
        df = df[df["phase"] == phase]

    if discipline != "All" and "discipline" in df.columns:
        df = df[df["discipline"] == discipline]

    # ---------------------------
    # KPI CALCULATIONS (SAFE)
    # ---------------------------
    total_items = len(df)
    high_risk = (df["risk_level"] == "High").sum()
    changes = df["change_flag"].sum()
    supplier_risk = relied_df["supplier"].sum()

    # ---------------------------
    # UI
    # ---------------------------
    st.title("🏗️ Design Intelligence Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Scope", total_items)
    col2.metric("High Risk", high_risk)
    col3.metric("Changes", changes)
    col4.metric("Supplier Dependency", supplier_risk)

    # ---------------------------
    # CHART
    # ---------------------------
    fig = px.histogram(df, x="risk_level", color="risk_level")
    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------
    # TABLE
    # ---------------------------
    st.dataframe(df, use_container_width=True)

    st.success("✅ Dashboard Ready")
