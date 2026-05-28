import streamlit as st

def apply_theme():
    st.markdown(
        """
        <style>

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #071e19 0%,
                #0b2e26 40%,
                #0f3d33 75%,
                #145c4a 100%
            );
            color: #e6f5f1;
        }

        /* Sidebar text */
        section[data-testid="stSidebar"] * {
            color: #e6f5f1 !important;
        }

        /* Section headers */
        .sidebar-section {
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #7fd1ba;
            margin-top: 10px;
            margin-bottom: 5px;
            font-weight: 600;
        }

        /* Divider */
        hr {
            border: 0.5px solid #2e6f60;
            margin: 10px 0;
        }

        /* Box styling (metrics & inputs) */
        .stMetric {
            background-color: rgba(255,255,255,0.05);
            padding: 10px;
            border-radius: 8px;
        }

        /* Inputs */
        .stSelectbox div,
        .stTextInput div {
            background-color: rgba(255,255,255,0.05) !important;
            border-radius: 6px;
        }

        /* Checkbox spacing */
        .stCheckbox {
            margin-bottom: 5px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )