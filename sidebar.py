import streamlit as st

def render_sidebar():
    # ---------------------------
    # HEADER
    # ---------------------------
    st.sidebar.title("🏗️ Design AI Platform")

    st.sidebar.markdown("""
    **Project:** Davyhulme ASP4  
    **Stage:** Feasibility  
    """)

    st.sidebar.markdown("---")

    # ---------------------------
    # NAVIGATION INFO
    # ---------------------------
    st.sidebar.subheader("📂 Navigation")

    st.sidebar.info("Use the menu above to switch pages")

    st.sidebar.markdown("""
    - 📊 Dashboard  
    - 📋 Scope  
    - 🔗 Sequence  
    - 📁 Relied Info  
    """)

    # ---------------------------
    # GLOBAL FILTERS
    # ---------------------------
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Filters")

    phase = st.sidebar.selectbox(
        "Phase",
        ["All", "40%", "60%", "Optimised 60%"]
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
        ]
    )

    # Store globally
    st.session_state["phase"] = phase
    st.session_state["discipline"] = discipline

    # ---------------------------
    # SYSTEM STATUS
    # ---------------------------
    st.sidebar.markdown("---")
    st.sidebar.subheader("🟢 System Status")

    st.sidebar.success("Data Loaded")
    st.sidebar.success("Risk Engine Active")
    st.sidebar.success("AI Ready")

    # ---------------------------
    # QUICK INSIGHTS
    # ---------------------------
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚡ Insights")

    st.sidebar.markdown("""
    - CHANGE events detected  
    - Supplier dependency present  
    - Higher risk in 60% phase  
    """)

    # ---------------------------
    # FOOTER
    # ---------------------------
    st.sidebar.markdown("---")
    st.sidebar.caption("Design Intelligence v1.0")