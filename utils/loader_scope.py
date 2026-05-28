import pandas as pd

def load_scope(path):

    # Try reading with header detection
    df = pd.read_excel(path, header=0)

    # Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Debug (you can remove later)
    print("Columns found:", df.columns.tolist())

    # Rename columns safely
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

    # Forward fill discipline (VERY important for your file)
    df["discipline"] = df["discipline"].ffill()

    # Ensure core columns exist
    for col in ["scope_item", "assumptions", "comments"]:
        if col not in df.columns:
            df[col] = ""

    # Drop empty rows
    df = df.dropna(how="all")

    # Add ID
    df["id"] = range(1, len(df) + 1)

    # Build text safely
    df["full_text"] = (
        df["scope_item"].astype(str) + " " +
        df["assumptions"].astype(str) + " " +
        df["comments"].astype(str)
    )

    return df