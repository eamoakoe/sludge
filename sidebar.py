import streamlit as st

def build_sidebar(scope_df):

    st.sidebar.markdown("### 🏗️ ASP4")
    st.sidebar.caption("Design Intelligence")

    st.sidebar.write("---")

    # SAFE discipline extraction
    if "discipline" in scope_df.columns:
        disciplines = sorted(scope_df["discipline"].dropna().unique())
    else:
        disciplines = []

    discipline = st.sidebar.selectbox(
        "Discipline",
        ["All"] + disciplines
    )

    search = st.sidebar.text_input("Search")

    st.sidebar.write("---")

    show_assumptions = st.sidebar.checkbox("Has Assumptions")
    show_changes = st.sidebar.checkbox("Show Changes")

    return {
        "discipline": discipline,
        "search": search,
        "assumptions": show_assumptions,
        "changes": show_changes
    }
