import streamlit as st

# ✅ Import your sidebar
from sidebar import render_sidebar

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Design Intelligence Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Render Sidebar
render_sidebar()

# ---------------------------
# HOME PAGE CONTENT
# ---------------------------

st.title("🏗️ Design Management Intelligence System")

st.markdown("""
Welcome to your AI-powered design dashboard.

### 🚀 What this platform does:
- Analyse design scope and risks  
- Track changes across phases  
- Understand dependencies and workflow  
- Highlight supplier and data risks  

---

### 📊 Navigate using the sidebar:
- Dashboard → overview and KPIs  
- Scope → detailed design items  
- Sequence → workflow and dependencies  
- Relied Info → external data and supplier inputs  
""")

# ---------------------------
# OPTIONAL: SIMPLE KPIs
# ---------------------------

col1, col2, col3 = st.columns(3)

col1.info("📊 Risk visibility across disciplines")
col2.info("🔗 Full design flow understanding")
col3.info("📁 External dependency tracking")

st.success("✅ System ready")
