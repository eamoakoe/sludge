import streamlit as st

def render_sidebar():

    st.sidebar.title("🏗️ Design AI Platform")

    st.sidebar.markdown("### Project")
    st.sidebar.write("Davyhulme ASP4")

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

    # store state (safe even if unused)
    st.session_state["phase"] = phase
    st.session_state["discipline"] = discipline

    st.sidebar.markdown("---")

    st.sidebar.success("✅ Sidebar Loaded")