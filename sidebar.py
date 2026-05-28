import streamlit as st

def build_sidebar(scope_df):

    # Header
    st.sidebar.markdown("### 🏗️ ASP4")
    st.sidebar.caption("Design Intelligence")

    st.sidebar.write("---")

    # Filters
    st.sidebar.markdown("#### 🔎 Scope Filters")

    disciplines = sorted(scope_df["discipline"].dropna().unique())

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + disciplines
    )

    search = st.sidebar.text_input("Search")

    st.sidebar.write("---")

    # Scope Quality
    st.sidebar.markdown("#### 🧾 Scope Quality")

    show_assumptions = st.sidebar.checkbox("Has Assumptions")
    show_changes = st.sidebar.checkbox("Show Changes Only")

    st.sidebar.write("---")

    # Risk
    st.sidebar.markdown("#### ⚠️ Risk")

    risk_filter = st.sidebar.multiselect(
        "Risk Level",
        ["High", "Medium", "Low"],
        default=["High", "Medium", "Low"]
    )

    uncertain_only = st.sidebar.checkbox("Uncertain Only")

    st.sidebar.write("---")

    # Summary
    total = len(scope_df)
    high = len(scope_df[scope_df["risk_level"] == "High"])

    st.sidebar.markdown("#### 📊 Summary")
    st.sidebar.metric("Items", total)
    st.sidebar.metric("High Risk", high)

    return {
        "discipline": discipline,
        "search": search,
        "risk": risk_filter,
        "assumptions": show_assumptions,
        "changes": show_changes,
        "uncertain": uncertain_only
    }