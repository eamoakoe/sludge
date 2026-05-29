import streamlit as st
import plotly.express as px

from utils.loader_scope import load_scope
from utils.risk_engine import calculate_risk, risk_level
from utils.text_utils import detect_change


def render_home():

    # ---------------------------
    # LOAD DATA
    # ---------------------------
    df = load_scope()

    # ---------------------------
    # AI PROCESSING
    # ---------------------------
    df["risk_score"] = df["full_text"].apply(calculate_risk)
    df["risk_level"] = df["risk_score"].apply(risk_level)
    df["change_flag"] = df["full_text"].apply(detect_change)

    # ---------------------------
    # APPLY FILTERS
    # ---------------------------
    phase = st.session_state.get("phase", "All")
    discipline = st.session_state.get("discipline", "All")

    if phase != "All":
        df = df[df["phase"] == phase]

    if discipline != "All":
        df = df[df["discipline"] == discipline]

    # ---------------------------
    # UI
    # ---------------------------
    st.title("🏗️ Design Intelligence Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Scope", len(df))
    col2.metric("High Risk", (df["risk_level"] == "High").sum())
    col3.metric("Changes", df["change_flag"].sum())
    col4.metric(
        "Assumptions",
        df["full_text"].str.contains("assume", case=False, na=False).sum()
    )

    # ---------------------------
    # CHARTS
    # ---------------------------
    fig = px.histogram(df, x="risk_level", color="risk_level")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(df, x="discipline", color="risk_level")
    st.plotly_chart(fig2, use_container_width=True)

    # ---------------------------
    # TABLE
    # ---------------------------
    st.dataframe(df, use_container_width=True)

    st.success("✅ Dashboard Ready")