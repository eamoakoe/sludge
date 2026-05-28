import streamlit as st

def build_sidebar(scope_df):

    # =====================================
    # HEADER
    # =====================================
    st.sidebar.markdown(
        """
        <div style="
            font-size:20px;
            font-weight:600;
            color:#e6f5f1;
        ">
            🏗️ ASP4
        </div>
        <div style="
            font-size:12px;
            color:#7fd1ba;
            margin-bottom:8px;
        ">
            Design Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # =====================================
    # NAVIGATION
    # =====================================
    st.sidebar.markdown(
        '<div class="sidebar-section">Modules</div>',
        unsafe_allow_html=True
    )

    page = st.sidebar.radio(
        "",
        [
            "Dashboard",
            "Scope",
            "Relied Info",
            "Sequence"
        ],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # =====================================
    # SCOPE FILTERS
    # =====================================
    st.sidebar.markdown(
        '<div class="sidebar-section">Scope Filters</div>',
        unsafe_allow_html=True
    )

    disciplines = []
    if "discipline" in scope_df.columns:
        disciplines = sorted(scope_df["discipline"].dropna().unique())

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + disciplines
    )

    phase = st.sidebar.selectbox(
        "Phase",
        ["All", "40%", "60%", "Optimised 60%"]
    )

    search = st.sidebar.text_input(
        "Search",
        placeholder="e.g. MBR, pumps..."
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # =====================================
    # SCOPE QUALITY (KEY FEATURE)
    # =====================================
    st.sidebar.markdown(
        '<div class="sidebar-section">Scope Quality</div>',
        unsafe_allow_html=True
    )

    show_assumptions = st.sidebar.checkbox("Has Assumptions")
    show_exclusions = st.sidebar.checkbox("Has Exclusions")
    show_comments = st.sidebar.checkbox("Has Comments")
    show_changes = st.sidebar.checkbox("Show Changes Only")

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # =====================================
    # RISK / UNCERTAINTY
    # =====================================
    st.sidebar.markdown(
        '<div class="sidebar-section">Uncertainty</div>',
        unsafe_allow_html=True
    )

    risk_levels = ["High", "Medium", "Low"]

    risk_filter = st.sidebar.multiselect(
        "Risk Level",
        risk_levels,
        default=risk_levels
    )

    uncertain_only = st.sidebar.checkbox(
        "Uncertain Items Only"
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # =====================================
    # SUMMARY (LIVE METRICS)
    # =====================================
    st.sidebar.markdown(
        '<div class="sidebar-section">Summary</div>',
        unsafe_allow_html=True
    )

    total_items = len(scope_df)

    high_risk = 0
    if "risk_level" in scope_df.columns:
        high_risk = len(scope_df[scope_df["risk_level"] == "High"])

    assumptions_count = 0
    if "assumptions" in scope_df.columns:
        assumptions_count = scope_df["assumptions"].notna().sum()

    col1, col2 = st.sidebar.columns(2)
    col1.metric("Items", total_items)
    col2.metric("High Risk", high_risk)

    st.sidebar.metric("With Assumptions", assumptions_count)

    st.sidebar.markdown("<hr>", unsafe_allow_html=True")

    # =====================================
    # AI CONTROLS
    # =====================================
    st.sidebar.markdown(
        '<div class="sidebar-section">Intelligence</div>',
        unsafe_allow_html=True
    )

    enable_ai = st.sidebar.toggle("AI Insights", True)

    # Footer
    st.sidebar.markdown(
        """
        <div style="
            font-size:11px;
            color:#7fd1ba;
            margin-top:10px;
        ">
            v1.0 | Design Manager Tool
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # RETURN FILTERS
    # =====================================
    return {
        "page": page,
        "discipline": discipline,
        "phase": phase,
        "search": search,
        "risk_filter": risk_filter,
        "show_assumptions": show_assumptions,
        "show_exclusions": show_exclusions,
        "show_comments": show_comments,
        "show_changes": show_changes,
        "uncertain_only": uncertain_only,
        "enable_ai": enable_ai
    }