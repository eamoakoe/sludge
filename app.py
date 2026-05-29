import streamlit as st

from sidebar import render_sidebar
from home import render_home

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Design Intelligence Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# SIDEBAR
# ---------------------------
render_sidebar()

# ---------------------------
# HOME PAGE
# ---------------------------
render_home()