from utils.loader_relied import load_relied

relied_df = load_relied()

# Example: supplier risk
supplier_risk = relied_df["supplier"].sum()

st.metric("Supplier Dependency (Veolia Docs)", supplier_risk)
