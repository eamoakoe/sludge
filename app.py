import sys
import os

# ✅ Fix imports for Streamlit Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd
from utils.loader_scope import load_scope
from utils.risk_engine import compute_risk
from utils.style import apply_theme
from sidebar import build_sidebar

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="ASP4 Design Dashboard",
    layout="wide"
)

# -----------------------------------
# STYLE
# -----------------------------------
apply_theme()

# -----------------------------------
# LOAD DATA (WITH FALLBACK)
# -----------------------------------
try:
    df = load_scope("data/design_scope.xlsx")
    df = compute_risk(df)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# -----------------------------------
# 🔍 FORCE DEBUG VISIBILITY
# -----------------------------------
st.subheader("🔍 Debug Info")

st.write("✅ Columns detected:")
st.write(df.columns.tolist())

st.write("✅ Total rows loaded:")
st.write(len(df))

st.write("✅ Sample raw data:")
st.dataframe(df.head(10), use_container_width=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------
filters = build_sidebar(df)

# -----------------------------------
# FILTERING (SAFE + STEP-BY-STEP)
# -----------------------------------
filtered = df.copy()

initial_count = len(filtered)

# Discipline
if "discipline" in filtered.columns and filters["discipline"] != "All":
    filtered = filtered[
        filtered["discipline"] == filters["discipline"]
    ]

st.write("After discipline filter:", len(filtered))

# Search
if filters["search"] and "scope_item" in filtered.columns:
    filtered = filtered[
        filtered["scope_item"].astype(str).str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

st.write("After search filter:", len(filtered))

# Assumptions
if filters["assumptions"] and "assumptions" in filtered.columns:
    filtered = filtered[
        filtered["assumptions"].astype(str).str.strip() != ""
    ]

st.write("After assumptions filter:", len(filtered))

# Changes
if filters["changes"] and "comments" in filtered.columns:
    filtered = filtered[
        filtered["comments"].astype(str).str.contains(
            "change",
            case=False,
            na=False
        )
    ]

st.write("After changes filter:", len(filtered))

# -----------------------------------
# FINAL DISPLAY
# -----------------------------------
st.markdown("---")
st.title("Design Scope")

if len(filtered) == 0:
    st.error("⚠️ No rows left after filtering")
    st.info("Showing FULL dataset instead to debug:")

    st.dataframe(df, use_container_width=True)
else:
    st.success(f"✅ Showing {len(filtered)} rows")
    st.dataframe(filtered, use_container_width=True)