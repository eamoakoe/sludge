import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd

st.set_page_config(page_title="ASP4", layout="wide")

st.title("DEBUG VIEW")

# ✅ Show working directory
st.write("Current working directory:")
st.write(os.getcwd())

# ✅ Show files in root
st.write("Files in root:")
st.write(os.listdir())

# ✅ Show files in asp/data folder
if os.path.exists("data"):
    st.write("Files in /data:")
    st.write(os.listdir("data"))
else:
    st.error("❌ data folder not found")

# ✅ Try loading Excel directly (no loader)
try:
    df = pd.read_excel("data/design_scope.xlsx")

    st.success("✅ Excel file loaded successfully")

    st.write("Columns:")
    st.write(df.columns.tolist())

    st.write("Row count:")
    st.write(len(df))

    st.write("Preview:")
    st.dataframe(df.head(20), width="stretch")

except Exception as e:
    st.error(f"❌ Error loading Excel: {e}")
``