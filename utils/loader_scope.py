import pandas as pd

def load_scope(path):
    df = pd.read_excel(path)

    # Clean headers
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Rename columns from your Excel
    rename_map = {
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    }

    df = df.rename(columns=rename_map)

    # Remove empty rows
    df = df.dropna(how="all")

    # Forward fill discipline
    if "discipline" in df.columns:
        df["discipline"] = df["discipline"].ffill()

    # Ensure required columns exist (prevents crash)
    for col in ["scope_item", "assumptions", "comments"]:
        if col not in df.columns:
            df[col] = ""

    # Add ID
    df["id"] = range(1, len(df) + 1)

    # ✅ SAFE FIX (no more astype crash)
    df["full_text"] = (
        df["scope_item"].astype(str) + " " +
        df["assumptions"].astype(str) + " " +
        df["comments"].astype(str)
    )

    return df