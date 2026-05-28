import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #071e19 0%,
            #0b2e26 50%,
            #145c4a 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: #e6f5f1 !important;
    }

    .sidebar-section {
        font-size: 12px;
        text-transform: uppercase;
        color: #7fd1ba;
        font-weight: 600;
    }

    hr {
        border: 0.5px solid #2e6f60;
    }

    </style>
    """, unsafe_allow_html=True)