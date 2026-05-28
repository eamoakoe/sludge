import streamlit as st

def build_sidebar(scope_df):

    # ====================================
    # 1. HEADER (Project Identity)
    # ====================================
    st.sidebar.markdown("### 🏗️ ASP4 Design")
    st.sidebar.caption("Design Intelligence Dashboard")

    st.sidebar.markdown("---")

    # ====================================
    # 2. NAVIGATION
    # ====================================
    st.sidebar.markdown("#### 📂 Modules")

    page = st.sidebar.radio(
        "",
        [
            "📊 Dashboard",
            "📋 Design Scope",
            "🔗 Relied Upon Info",
            "📅 Design Sequence"
        ],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")

    # ====================================
    # 3. CORE FILTERS (Scope-driven)
    # ====================================
    st.sidebar.markdown("#### 🔎 Filters")

    # Discipline
    if "discipline" in scope_df.columns:
        disciplines = sorted(scope_df["discipline"].dropna().unique())
    else:
        disciplines = []

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + list(disciplines)
    )

    # Phase (fixed for now)
    phase = st.sidebar.selectbox(
        "Design Phase",
        ["All", "40%", "60%", "Optimised 60%"]
    )

    # Search
    search = st.sidebar.text_input(
        "Search",
        placeholder="e.g. pumps, MBR, pipeline..."
    )

    st.sidebar.markdown("---")

    # ====================================
    # 4. RISK & INSIGHT FILTERS
    # ====================================
    st.sidebar.markdown("#### ⚠️ Risk & Insights")

    if "risk_level" in scope_df.columns:
        risk_levels = sorted(scope_df["risk_level"].dropna().unique())
    else:
        risk_levels = ["High", "Medium", "Low"]

    risk_filter = st.sidebar.multiselect(
        "Risk Level",
        options=risk_levels,
        default=risk_levels
    )

    # Optional: show only uncertain scope
    show_uncertain = st.sidebar.checkbox(
        "Show only uncertain items (TBC / Assumptions)"
    )

    st.sidebar.markdown("---")

    # ====================================
    # 5. LIVE SUMMARY (very important)
    # ====================================
    st.sidebar.markdown("#### 📈 Summary")

    total_items = len(scope_df)
    high_risk = len(scope_df[scope_df.get("risk_level", "") == "High"])

    col1, col2 = st.sidebar.columns(2)
    col1.metric("Items", total_items)
    col2.metric("High Risk", high_risk)

    st.sidebar.markdown("---")

    # ====================================
    # 6. SYSTEM CONTROLS (AI)
    # ====================================
    st.sidebar.markdown("#### 🤖 Intelligence")

    enable_ai = st.sidebar.toggle(
        "AI Insights",
        value=True
    )

    # Future toggle placeholder
    show_dependencies = st.sidebar.checkbox(
        "Show Dependencies (coming soon)",
        disabled=True
    )

    # ====================================
    # RETURN FILTER CONFIG
    # ====================================
    return {
        "page": page,
        "discipline": discipline,
        "phase": phase,
        "risk_filter": risk_filter,
        "search": search,
        "show_uncertain": show_uncertain,
        "enable_ai": enable_ai
    }