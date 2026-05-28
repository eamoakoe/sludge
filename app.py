import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.loader_scope import load_scope
from utils.style import apply_theme
from sidebar import build_sidebar

st.set_page_config(page_title="ASP4", layout="wide")

apply_theme()

# ✅ Load correctly structured data
df = load_scope("data/design_scope.xlsx")

# ✅ Sidebar
filters = build_sidebar(df)

# ✅ Filtering
filtered = df.copy()

if filters["discipline"] != "All":
    filtered = filtered[filtered["discipline"] == filters["discipline"]]

if filters["search"]:
    filtered = filtered[
        filtered["scope_item"].astype(str).str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

if filters["assumptions"]:
    filtered = filtered[
        filtered["assumptions"].astype(str).str.strip() != ""
    ]

if filters["changes"]:
    filtered = filtered[
        filtered["comments"].astype(str).str.contains(
            "change",
            case=False,
            na=False
        )
    ]

# ✅ Always show something
st.title("Design Scope")

if len(filtered) == 0:
    st.warning("No matching results — showing full dataset")
    st.dataframe(df, width="stretch")
else:
    st.dataframe(filtered, width="stretch")
