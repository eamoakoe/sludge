import pandas as pd

def load_scope():
    df = pd.read_excel("data/design_scope.xlsx", engine="openpyxl")

    # Clean column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Forward fill discipline
    if "discipline" in df.columns:
        df["discipline"] = df["discipline"].ffill()

    # ---- CREATE full_text SAFELY ----
    text_cols = [
        "scope item",
        "assumptions / clarifications",
        "exclusions",
        "arup comments"
    ]

    # Keep only existing columns
    existing_cols = [c for c in text_cols if c in df.columns]

    if existing_cols:
        df["full_text"] = df[existing_cols].fillna("").astype(str).agg(" ".join, axis=1)
    else:
        df["full_text"] = ""   # fallback

    return df
