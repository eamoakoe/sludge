from utils.style import apply_theme
from utils.loader_scope import load_scope
from utils.risk_engine import compute_risk
from sidebar import build_sidebar

# Apply theme FIRST
apply_theme()

# Load scope data
scope_df = load_scope("data/design_scope.xlsx")
scope_df = compute_risk(scope_df)

# Sidebar
filters = build_sidebar(scope_df)