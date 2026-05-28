import sys
import os

# ✅ Fix import paths (CRITICAL for Streamlit Cloud)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.loader_scope import load_scope
from utils.risk_engine import compute_risk
from utils.style import apply_theme
from sidebar import build_sidebar

# ✅ Page config (clean UI)
st.set_page_config(
    page_title="ASP4 Design Dashboard",
    layout="wide"
)

# ✅ Apply dark green theme
apply_theme()

# ✅ Load data
df = load_scope("data/design_scope.xlsx")
df = compute_risk(df)

# ✅ Sidebar (minimal version)
filters = build_sidebar(df)

# -----------------------------------
# ✅ FILTER LOGIC
# -----------------------------------
filtered = df.copy()

# Discipline filter
if filters["discipline"] != "All":
    filtered = filtered[
        filtered["discipline"] == filters["discipline"]
    ]

# Search filter
if filters["search"]:
    filtered = filtered[
        filtered["scope_item"].str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

# Assumptions filter
if filters["assumptions"]:
    filtered = filtered[
        filtered["assumptions"].astype(str).str.strip() != ""
    ]

# Changes filter (based on comments text)
if filters["changes"]:
    filtered = filtered[
        filtered["comments"].astype(str).str.contains(
            "change",
            case=False,
            na=False
        )
    ]

# -----------------------------------
# ✅ MAIN UI
# -----------------------------------
st.title("Design Scope")

st.markdown(
    """
    <div style='font-size:14px; color:#7fd1ba;'>
        Filter and explore design scope items
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ Clean table display
st.dataframe(
    filtered,
    use_container_width=True,
    height=600
)