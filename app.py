import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="Design Intelligence Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Sidebar Branding ----
st.sidebar.title("🏗️ Design AI Platform")

st.sidebar.markdown("""
**Project:** Davyhulme ASP4  
**Phase:** Feasibility  
**Built by:** Design Management  

---
""")

# ---- Navigation Info ----
st.sidebar.subheader("📂 Modules")

st.sidebar.markdown("""
- 📊 Dashboard  
- 📋 Scope Analysis  
- 🔗 Design Sequence  
- 📁 Relied Information  
""")

# ---- Global Filters (OPTIONAL but powerful) ----
st.sidebar.subheader("⚙️ Global Filters")

phase = st.sidebar.selectbox(
    "Select Phase",
    ["All", "40%", "60%", "Optimised 60%"]
)

discipline = st.sidebar.selectbox(
    "Select Discipline",
    ["All", "Civil", "Structural", "Mechanical", "Process", "Electrical & ICA"]
)

# Store globally (important)
st.session_state["phase"] = phase
st.session_state["discipline"] = discipline

# ---- Main Page ----
st.title("🏗️ Design Management Intelligence System")

st.markdown("""
Welcome to the AI-powered design dashboard.

Use the sidebar to navigate between:
- **Scope Intelligence**
- **Design Flow**
- **Dependency Risk**

---

### 🚀 What this tool does
- Detects **design risks automatically**
- Highlights **changes in scope**
- Tracks **dependencies and bottlenecks**
- Surfaces **supplier and data risks**

---
""")

# ---- Quick Summary Panel ----
col1, col2, col3 = st.columns(3)

col1.info("📊 Analyse design risk across disciplines")
col2.info("🔗 Understand sequencing and dependencies")
col3.info("📁 Track relied information & supplier exposure")

st.success("✅ System ready")
