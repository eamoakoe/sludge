import sys
import os

# ✅ Fix import paths (CRITICAL for Streamlit Cloud)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.loader_scope import load_scope
from utils.risk_engine import compute_risk
from utils.style import apply_theme
from sidebar import build_sidebar

# -----------------------------------
# ✅ PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="ASP4 Design Dashboard",
    layout="wide"
)

# -----------------------------------
# ✅ THEME
# -----------------------------------
apply_theme()

# -----------------------------------
# ✅ LOAD DATA
# -----------------------------------
df = load_scope("data/design_scope.xlsx")
df = compute_risk(df)

# Debug (remove later if you want)
st.write("Columns:", df.columns.tolist())
st.write("Total rows loaded:", len(df))

# -----------------------------------
# ✅ SIDEBAR
# -----------------------------------
filters = build_sidebar(df)

# -----------------------------------
# ✅ FILTER DATA (SAFE VERSION)
# -----------------------------------
filtered = df.copy()

# Discipline filter
if filters["discipline"] != "All" and "discipline" in filtered.columns:
    filtered = filtered[
        filtered["discipline"] == filters["discipline"]
    ]

# Search filter
if filters["search"] and "scope_item" in filtered.columns:
    filtered = filtered[
        filtered["scope_item"].astype(str).str.contains(
            filters["search"],
            case=False,
            na=False
        )
    ]

# Assumptions filter
if filters["assumptions"] and "assumptions" in filtered.columns:
    filtered = filtered[
        filtered["assumptions"].astype(str).str.strip() != ""
    ]

# Changes filter
if filters["changes"] and "comments" in filtered.columns:
    filtered = filtered[
        filtered["comments"].astype(str).str.contains(
            "change",
            case=False,
            na=False
        )
    ]

# -----------------------------------
# ✅ DEBUG ROW COUNTS
# -----------------------------------
st.write("Rows after filtering:", len(filtered))

# -----------------------------------
# ✅ UI DISPLAY
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

# ✅ Handle empty results
if filtered.empty:
    st.warning("No data matches current filters")

    st.markdown("Showing sample data for reference:")
    st.dataframe(df.head(20), use_container_width=True)

else:
    st.dataframe(
        filtered,
        use_container_width=True,
        height=600
    )