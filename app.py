import streamlit as st
from sidebar import render_sidebar

# Page config
st.set_page_config(
    page_title="Test Sidebar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Render ONLY sidebar
render_sidebar()

# Main area (empty test)
st.title("✅ Sidebar Test Page")
st.write("If you can see the sidebar, everything is working.")