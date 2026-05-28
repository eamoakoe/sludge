from utils.loader_scope import load_scope
from utils.risk_engine import compute_risk
from sidebar import build_sidebar

# Load scope (single source for now)
scope_df = load_scope("data/design_scope.xlsx")
scope_df = compute_risk(scope_df)

# Build sidebar
filters = build_sidebar(scope_df)

# Example usage
filtered_df = scope_df.copy()

if filters["discipline"] != "All":
    filtered_df = filtered_df[filtered_df["discipline"] == filters["discipline"]]

if filters["risk_filter"]:
    filtered_df = filtered_df[filtered_df["risk_level"].isin(filters["risk_filter"])]

if filters["search"]:
    filtered_df = filtered_df[
        filtered_df["scope_item"].str.contains(filters["search"], case=False, na=False)
    ]