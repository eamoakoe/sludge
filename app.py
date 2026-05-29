import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.loader_scope import load_scope
from sidebar import build_sidebar
from utils.style import apply_theme

# CONFIG
st.set_page_config(page_title="ASP4", layout="wide")

apply_theme()

st.title("Design Scope Dashboard")

# ✅ Load data
df = load_scope("data/design_scope.xlsx")

st.write(f"✅ Loaded {len(df)} scope items")

# ✅ Sidebar
filters = build_sidebar(df)

# ✅ Filtering logic
filtered = df.copy()

# Discipline
if filters["discipline"] != "All":
    filtered = filtered[
        filtered["discipline"] == filters["discipline"]
    ]

# Search
if filters["search"]:
    filtered = filtered[
        filtered["scope_item"].str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

# Assumptions
if filters["assumptions"]:
    filtered = filtered[
        filtered["assumptions"].str.strip() != ""
    ]

# Changes
if filters["changes"]:
    filtered = filtered[
        filtered["comments"].str.contains(
            "change",
            case=False,
            na=False
        )
    ]

# ✅ Always display something
if filtered.empty:
    st.warning("No matches — showing full dataset")
    st.dataframe(df, width="stretch")
else:
    st.dataframe(filtered, width="stretch")