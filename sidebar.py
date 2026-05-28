import streamlit as st

def build_sidebar(scope_df):

    # ------------------------------------
    # HEADER
    # ------------------------------------
    st.sidebar.markdown(
        """
        <div style="font-size:20px; font-weight:600;">
            🏗️ ASP4
        </div>
        <div style="font-size:12px; color:#9fded0;">
            Design Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # ------------------------------------
    # NAVIGATION
    # ------------------------------------
    st.sidebar.markdown('<div class="sidebar-section">Modules</div>', unsafe_allow_html=True)

    page = st.sidebar.radio(
        "",
        [
            "Dashboard",
            "Design Scope",
            "Relied Upon Info",
            "Design Sequence"
        ],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # ------------------------------------
    # FILTERS
    # ------------------------------------
    st.sidebar.markdown('<div class="sidebar-section">Filters</div>', unsafe_allow_html=True)

    # Discipline (dynamic)
    disciplines = []
    if "discipline" in scope_df.columns:
        disciplines = sorted(scope_df["discipline"].dropna().unique())

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + list(disciplines)
    )

    phase = st.sidebar.selectbox(
        "Phase",
        ["All", "40%", "60%", "Optimised 60%"]
    )

    search = st.sidebar.text_input(
        "Search",
        placeholder="Type keywords..."
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # ------------------------------------
    # RISK / INSIGHT
    # ------------------------------------
    st.sidebar.markdown('<div class="sidebar-section">Risk & Insights</div>', unsafe_allow_html=True)

    if "risk_level" in scope_df.columns:
        risk_levels = sorted(scope_df["risk_level"].dropna().unique())
    else:
        risk_levels = ["High", "Medium", "Low"]

    risk_filter = st.sidebar.multiselect(
        "Risk Level",
        options=risk_levels,
        default=risk_levels
    )

    show_uncertain = st.sidebar.checkbox("Uncertain Items Only")

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # ------------------------------------
    # SUMMARY
    # ------------------------------------
    st.sidebar.markdown('<div class="sidebar-section">Summary</div>', unsafe_allow_html=True)

    total_items = len(scope_df)
    high_risk = len(scope_df[scope_df.get("risk_level", "") == "High"])

    col1, col2 = st.sidebar.columns(2)
    col1.metric("Items", total_items)
    col2.metric("High Risk", high_risk)

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # ------------------------------------
    # AI CONTROLS
    # ------------------------------------
    st.sidebar.markdown('<div class="sidebar-section">Intelligence</div>', unsafe_allow_html=True)

    enable_ai = st.sidebar.toggle("AI Insights", value=True)

    st.sidebar.markdown(
        '<div style="font-size:11px; color:#9fded0;">v1.0 | Design Manager Tool</div>',
        unsafe_allow_html=True
    )

    return {
        "page": page,
        "discipline": discipline,
        "phase": phase,
        "risk_filter": risk_filter,
        "search": search,
        "show_uncertain": show_uncertain,
        "enable_ai": enable_ai
    }