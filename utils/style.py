import streamlit as st

def apply_theme():
    st.markdown(
        """
        <style>
        /* Main sidebar background */
        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg, 
                #0b2e26 0%, 
                #0f3d33 50%, 
                #145c4a 100%
            );
            color: #e6f5f1;
        }

        /* Sidebar text */
        section[data-testid="stSidebar"] * {
            color: #e6f5f1;
        }

        /* Section headers */
        .sidebar-section {
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #8fd3c1;
            margin-top: 10px;
            margin-bottom: 5px;
        }

        /* Divider */
        hr {
            border: 0.5px solid #2f6f5e;
            margin: 10px 0;
        }

        /* Metric styling */
        [data-testid="stMetric"] {
            background-color: rgba(255,255,255,0.05);
            padding: 10px;
            border-radius: 8px;
        }

        /* Input fields */
        .stSelectbox, .stTextInput {
            background-color: rgba(255,255,255,0.05);
            border-radius: 6px;
        }

        /* Buttons / radio */
        .stRadio > div {
            gap: 6px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )