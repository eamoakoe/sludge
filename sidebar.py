import streamlit as st


def render_sidebar():
    # =========================
    # TITLE / BRANDING
    # =========================
    st.sidebar.title("🏗️ Design AI Platform")

    st.sidebar.markdown("""
    **Project:** Davyhulme ASP4  
    **Phase:** Feasibility  
    """)

    st.sidebar.markdown("---")

    # =========================
    # NAVIGATION INFO
    # =========================
    st.sidebar.subheader("📂 Navigation")

    st.sidebar.info("Use the page selector above to switch modules")

    st.sidebar.markdown("""
    - Home (Dashboard)  
    - Scope  
    - Sequence  
    - Relied Info  
    """)

    # =========================
    # GLOBAL FILTERS (CORE)
    # =========================
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Filters")

    # ---- Phase Filter ----
    phase = st.sidebar.selectbox(
        "Phase",
        ["All", "40%", "60%", "Optimised 60%"],
        key="phase_filter"
    )

    # ---- Discipline Filter ----
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

    # ✅ STORE GLOBALLY (THIS IS THE MOST IMPORTANT PART)
    st.session_state["phase"] = phase
    st.session_state["discipline"] = discipline

    # =========================
    # SYSTEM STATUS
    # =========================
    st.sidebar.markdown("---")
    st.sidebar.subheader("🟢 System Status")

    st.sidebar.success("App Running")
