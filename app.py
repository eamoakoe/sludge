import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.loader_scope import load_scope
from utils.style import apply_theme
from sidebar import build_sidebar

# Page config
st.set_page_config(page_title="ASP4 Design Dashboard", layout="wide")

# Style
apply_theme()

# Load data
df = load_scope("data/design_scope.xlsx")

# Sidebar
filters = build_sidebar(df)

# ---------------------------
# FILTERING (SAFE)
# ---------------------------
filtered = df.copy()

# Discipline
if filters["discipline"] != "All":
    filtered = filtered[
        filtered["discipline"] == filters["discipline"]
    ]

# Search
if filters["search"]:
    filtered = filtered[
        filtered["scope_item"].astype(str).str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

# Assumptions
if filters["assumptions"]:
    filtered = filtered[
        filtered["assumptions"].astype(str).str.strip() != ""
    ]

# Changes
if filters["changes"]:
    filtered = filtered[
        filtered["comments"].astype(str).str.contains(
            "change",
            case=False,
            na=False
        )
    ]

# ---------------------------
# DISPLAY
# ---------------------------
st.title("Design Scope")

# ✅ ALWAYS show something
if len(filtered) == 0:
    st.warning("No data found with current filters")
    st.info("Showing full dataset instead")
    st.dataframe(df, use_container_width=True)
else:
    st.dataframe(filtered, use_container_width=True)