import streamlit as st

def build_sidebar(scope_df):

    st.sidebar.markdown("### 🏗️ ASP4")
    st.sidebar.caption("Design Intelligence")

    st.sidebar.write("---")

    # ✅ Get REAL disciplines only
    disciplines = sorted(
        scope_df["discipline"]
        .dropna()
        .unique()
        .tolist()
    )

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + disciplines
    )

    # ✅ Search
    search = st.sidebar.text_input("Search")

    st.sidebar.write("---")

    # ✅ Only show filters if relevant data exists
    has_assumptions = (
        scope_df["assumptions"].str.strip() != ""
    ).any()

    has_changes = (
        scope_df["comments"].str.contains("change", case=False, na=False)
    ).any()

    show_assumptions = False
    show_changes = False

    if has_assumptions:
        show_assumptions = st.sidebar.checkbox("Has Assumptions")

    if has_changes:
        show_changes = st.sidebar.checkbox("Show Changes")

    return {
        "discipline": discipline,
        "search": search,
        "assumptions": show_assumptions,
        "changes": show_changes
    }