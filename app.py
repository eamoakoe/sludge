import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd
from utils.loader_scope import load_scope
from sidebar import build_sidebar
from utils.style import apply_theme

st.set_page_config(page_title="ASP4", layout="wide")

apply_theme()

st.title("Design Scope Dashboard")

# -----------------------------------
# LOAD DATA SAFELY
# -----------------------------------
try:
    df = load_scope("data/design_scope.xlsx")
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# -----------------------------------
# SHOW BASIC INFO (ALWAYS visible)
# -----------------------------------
st.write("✅ Columns:", df.columns.tolist())
st.write("✅ Rows:", len(df))

# -----------------------------------
# SIDEBAR
# -----------------------------------
filters = build_sidebar(df)

# -----------------------------------
# SAFE FILTERING
# -----------------------------------
filtered = df.copy()

# Discipline
if "discipline" in filtered.columns and filters["discipline"] != "All":
    filtered = filtered[filtered["discipline"] == filters["discipline"]]

# Search
if "scope_item" in filtered.columns and filters["search"]:
    filtered = filtered[
        filtered["scope_item"].astype(str).str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

# Assumptions
if "assumptions" in filtered.columns and filters["assumptions"]:
    filtered = filtered[
        filtered["assumptions"].astype(str).str.strip() != ""
    ]

# Changes
if "comments" in filtered.columns and filters["changes"]:
    filtered = filtered[
        filtered["comments"].astype(str).str.contains(
            "change",
            case=False,
            na=False
        )
    ]

# -----------------------------------
# DISPLAY DATA (NEVER EMPTY SCREEN)
# -----------------------------------
if filtered.empty:
    st.warning("⚠️ No rows match filters — showing full dataset instead")
    st.dataframe(df, width="stretch")
else:
    st.success(f"✅ Showing {len(filtered)} rows")
    st.dataframe(filtered, width="stretch")
