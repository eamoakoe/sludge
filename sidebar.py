import streamlit as st

def build_sidebar(scope_df):

    # --------------------------
    # HEADER
    # --------------------------
    st.sidebar.markdown("### 🏗️ ASP4")
    st.sidebar.caption("Design Intelligence")

    st.sidebar.write("---")

    # --------------------------
    # FILTERS (ONLY ESSENTIAL)
    # --------------------------
    st.sidebar.markdown("#### 🔎 Filters")

    # Discipline
    if "discipline" in scope_df.columns:
        disciplines = sorted(scope_df["discipline"].dropna().unique())
    else:
        disciplines = []

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + disciplines
    )

    # Search
    search = st.sidebar.text_input(
        "Search",
        placeholder="e.g. pumps, MBR..."
    )

    st.sidebar.write("---")

    # --------------------------
    # SCOPE QUALITY ONLY
    # --------------------------
    st.sidebar.markdown("#### 🧾 Scope")

    show_assumptions = st.sidebar.checkbox("Has Assumptions")
    show_changes = st.sidebar.checkbox("Show Changes")

    # --------------------------
    # RETURN FILTERS
    # --------------------------
    return {
        "discipline": discipline,
        "search": search,
        "assumptions": show_assumptions,
        "changes": show_changes
    }