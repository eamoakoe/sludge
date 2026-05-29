import streamlit as st

def render_home():

    st.title("🏗️ Home Page")

    st.markdown("""
    This is a placeholder home page.

    ✅ Sidebar should load independently  
    ✅ No data is being loaded  
    ✅ No risk calculations running  
    """)

    # Show current filter values (to confirm sidebar works)
    phase = st.session_state.get("phase", "Not set")
    discipline = st.session_state.get("discipline", "Not set")

    st.subheader("🔎 Current Filters")

    st.write(f"Phase: {phase}")
    st.write(f"Discipline: {discipline}")
