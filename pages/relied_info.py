import streamlit as st
import plotly.express as px

from utils.loader_relief import load_relied

st.title("📁 Relied Upon Information")

df = load_relied()

# ---- KPIs ----
col1, col2, col3 = st.columns(3)

col1.metric("Total Documents", len(df))
col2.metric("Supplier Proposals", (df["category"] == "Supplier Proposal").sum())
col3.metric("Risky Docs", df["risk_flag"].sum())

# ---- Chart: Categories ----
fig = px.pie(df, names="category")
st.plotly_chart(fig, use_container_width=True)

# ---- Chart: Sites ----
fig2 = px.bar(df, x="site")
st.plotly_chart(fig2, use_container_width=True)

# ---- Table ----
st.dataframe(df)
