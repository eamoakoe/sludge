import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Design Intelligence Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SIDEBAR
# =========================

# ---- Header / Branding ----
st.sidebar.title("🏗️ Design AI Platform")

st.sidebar.markdown("""
**Project:** Davyhulme ASP4  
**Module:** Feasibility Design  
**System:** AI Design Management  

---
""")

# =========================
# NAVIGATION GUIDE
# =========================
st.sidebar.subheader("📂 Navigation")

st.sidebar.markdown("""
Use the built-in page menu:

- 📊 Dashboard  
- 📋 Scope Analysis  
- 🔗 Design Sequence  
- 📁 Relied Information  
""")

# Optional quick nav buttons (works in Streamlit Cloud)
st.sidebar.markdown("### 🚀 Quick Access")

try:
    if st.sidebar.button("📊 Dashboard"):
        st.switch_page("pages/dashboard.py")

    if st.sidebar.button("📋 Scope"):
        st.switch_page("pages/scope.py")

    if st.sidebar.button("🔗 Sequence"):
        st.switch_page("pages/sequence.py")

    if st.sidebar.button("📁 Relied Info"):
        st.switch_page("pages/relied_info.py")
except:
    # fallback for local dev or older Streamlit versions
    st.sidebar.info("Use sidebar page selector")

# =========================
# GLOBAL FILTERS
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Global Filters")

# Phase filter
phase = st.sidebar.selectbox(
    "Select Phase",
    ["All", "40%", "60%", "Optimised 60%"],
    index=0
)

# Discipline filter
discipline = st.sidebar.selectbox(
    "Select Discipline",
    [
        "All",
        "Civil",
        "Structural",
        "Mechanical",
        "Process",
        "Electrical & ICA",
        "Geotechnical"
    ],
    index=0
)

# Store globally across pages
st.session_state["phase"] = phase
st.session_state["discipline"] = discipline

# =========================
# SYSTEM STATUS
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("🟢 System Status")

st.sidebar.success("Data Loaded")
st.sidebar.success("Risk Engine Active")
st.sidebar.success("AI Layer Running")

# =========================
# QUICK INSIGHTS (STATIC OR DYNAMIC)
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("⚡ Quick Insights")

st.sidebar.markdown("""
- Multiple **CHANGE events** detected  
- Heavy reliance on **supplier proposals**  
- Risk concentration in **60% phase**  
""")

# =========================
# OPTIONAL METRICS PREVIEW
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Snapshot")

# Placeholder values (replace later with real calculations)
st.sidebar.metric("Scope Items", "—")
st.sidebar.metric("High Risk Items", "—")
st.sidebar.metric("Change Events", "—")

# =========================
# FOOTER
# =========================
st.sidebar.markdown("---")
st.sidebar.caption("Design Intelligence System v1.0")
