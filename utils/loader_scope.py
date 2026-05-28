import pandas as pd

def load_scope(path):
    df = pd.read_excel(path)

    df.columns = [str(col).strip().lower() for col in df.columns]

    rename_map = {
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    }

    df = df.rename(columns=rename_map)

    df = df.dropna(how="all")

    if "discipline" in df.columns:
        df["discipline"] = df["discipline"].ffill()

    df["id"] = range(1, len(df) + 1)

    # ✅ Ensure columns always exist
    required_cols = ["scope_item", "assumptions", "comments"]

    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    # ✅ Now safe to use astype
    df["full_text"] = (
            df["scope_item"].astype(str) + " " +
            df["assumptions"].astype(str) + " " +
            df["comments"].astype(str)
    )

    return df