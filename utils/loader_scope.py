import pandas as pd

def load_scope(path):

    df = pd.read_excel(path)

    # Clean headers
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Rename to clean names
    rename_map = {
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    }

    df = df.rename(columns=rename_map)

    # ✅ Ensure discipline exists
    if "discipline" not in df.columns:
        df["discipline"] = "Unknown"

    # Forward fill discipline
    df["discipline"] = df["discipline"].ffill()

    # Ensure key columns exist
    for col in ["scope_item", "assumptions", "comments"]:
        if col not in df.columns:
            df[col] = ""

    df = df.dropna(how="all")

    # Add ID
    df["id"] = range(1, len(df) + 1)

    # Combine text
    df["full_text"] = (
        df["scope_item"].astype(str) + " " +
        df["assumptions"].astype(str) + " " +
        df["comments"].astype(str)
    )

    return df