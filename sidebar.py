import streamlit as st

def render_sidebar():
    # =========================
    # HEADER / BRANDING
    # =========================
    st.sidebar.title("🏗️ Design AI Platform")

    st.sidebar.markdown("""
**Project:** Davyhulme ASP4  
**Stage:** Feasibility  
""")

    st.sidebar.markdown("---")

    # =========================
    # NAVIGATION INFO
    # =========================
    st.sidebar.subheader("📂 Navigation")

    st.sidebar.info("Use the page selector above to switch screens")

    st.sidebar.markdown("""
- Home (Dashboard)  
- Scope  
- Sequence  
- Relied Info  
""")

    # =========================
    # GLOBAL FILTERS
    # =========================
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Filters")

    phase = st.sidebar.selectbox(
        "Phase",
        ["All", "40%", "60%", "Optimised 60%"],
        key="phase_filter"
    )

    discipline = st.sidebar.selectbox(
        "Discipline",
        [
            "All",
            "Civil",
            "Structural",
            "Mechanical",
            "Process",
            "Electrical & ICA",
            "Geotechnical"
        ],
        key="discipline_filter"
    )

    # Save filters globally (used by all pages)
    st.session_state["phase"] = phase
    st.session_state["discipline"] = discipline

    # =========================
    # SYSTEM STATUS
    # =========================
    st.sidebar.markdown("---")
    st.sidebar.subheader("🟢 System Status")

    st.sidebar.success("Data Loaded")
    st.sidebar.success("Risk Engine Active")
    st.sidebar.success("App Running")

    # =========================
    # QUICK INSIGHTS (STATIC FOR NOW)
    # =========================
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚡ Insights")

    st.sidebar.markdown("""
- Changes detected in scope  
- Supplier dependency present  
- Risk concentrated in later phases  
""")

    # =========================
    # FOOTER
    # =========================
    st.sidebar.markdown("---")
    st.sidebar.caption("Design Intelligence System v1.0")