import streamlit as st

def build_sidebar(scope_df):

    st.sidebar.markdown("### 🏗️ ASP4")
    st.sidebar.caption("Design Intelligence")

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # NAV
    st.sidebar.markdown('<div class="sidebar-section">Modules</div>', unsafe_allow_html=True)

    page = st.sidebar.radio(
        "",
        ["Dashboard", "Scope", "Relied Info", "Sequence"],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # FILTERS
    st.sidebar.markdown('<div class="sidebar-section">Scope Filters</div>', unsafe_allow_html=True)

    disciplines = sorted(scope_df["discipline"].dropna().unique())

    discipline = st.sidebar.selectbox("Discipline", ["All"] + disciplines)

    phase = st.sidebar.selectbox("Phase", ["All", "40%", "60%", "Optimised 60%"])

    search = st.sidebar.text_input("Search")

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # QUALITY
    st.sidebar.markdown('<div class="sidebar-section">Scope Quality</div>', unsafe_allow_html=True)

    show_assumptions = st.sidebar.checkbox("Has Assumptions")
    show_changes = st.sidebar.checkbox("Show Changes Only")

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # RISK
    st.sidebar.markdown('<div class="sidebar-section">Risk</div>', unsafe_allow_html=True)

    risk_filter = st.sidebar.multiselect(
        "Risk Level",
        ["High", "Medium", "Low"],
        default=["High", "Medium", "Low"]
    )

    uncertain_only = st.sidebar.checkbox("Uncertain Only")

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # SUMMARY
    total = len(scope_df)
    high = len(scope_df[scope_df["risk_level"] == "High"])

    st.sidebar.markdown('<div class="sidebar-section">Summary</div>', unsafe_allow_html=True)
    st.sidebar.metric("Items", total)
    st.sidebar.metric("High Risk", high)

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # AI
    st.sidebar.toggle("AI Insights", True)

    return {
        "page": page,
        "discipline": discipline,
        "phase": phase,
        "search": search,
        "risk": risk_filter,
        "assumptions": show_assumptions,
        "changes": show_changes,
        "uncertain": uncertain_only
    }