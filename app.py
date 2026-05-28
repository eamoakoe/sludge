import sys
import os

# ✅ CRITICAL FIX FOR STREAMLIT CLOUD
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.loader_scope import load_scope
from utils.risk_engine import compute_risk
from utils.style import apply_theme
from sidebar import build_sidebar

# Apply theme
apply_theme()

# Load data
df = load_scope("data/design_scope.xlsx")
df = compute_risk(df)

# Sidebar
filters = build_sidebar(df)

# --------------------
# FILTER LOGIC
# --------------------
filtered = df.copy()

if filters["discipline"] != "All":
    filtered = filtered[filtered["discipline"] == filters["discipline"]]

if filters["risk"]:
    filtered = filtered[filtered["risk_level"].isin(filters["risk"])]

if filters["uncertain"]:
    filtered = filtered[filtered["is_uncertain"] == True]

if filters["search"]:
    filtered = filtered[
        filtered["scope_item"].str.contains(filters["search"], case=False, na=False)
    ]

# ✅ Assumptions filter
if filters["assumptions"]:
    filtered = filtered[filtered["assumptions"].notna()]

# ✅ Changes filter
if filters["changes"]:
    filtered = filtered[
        filtered["comments"].str.contains("change", case=False, na=False)
    ]

# --------------------
# UI
# --------------------
st.title("Design Scope")

st.dataframe(filtered, use_container_width=True)