import pandas as pd

def load_scope():
    df = pd.read_excel("data/design_scope.xlsx", engine="openpyxl")

    # ---- Clean column names ----
    df.columns = [c.strip().lower() for c in df.columns]

    # ---- Fix hierarchy (discipline forward fill) ----
    if "discipline" in df.columns:
        df["discipline"] = df["discipline"].ffill()

    # ---- Create FULL TEXT COLUMN (THIS FIXES YOUR ERROR) ----
    text_cols = [
        "scope item",
        "assumptions / clarifications",
        "exclusions",
        "arup comments"
    ]

    # Only keep columns that exist
    existing_cols = [c for c in text_cols if c in df.columns]

    df["full_text"] = df[existing_cols].fillna("").agg(" ".join, axis=1)

    return df