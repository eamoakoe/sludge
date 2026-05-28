import pandas as pd

def load_scope(file_path):
    df = pd.read_excel(file_path)

    # Clean column names
    df.columns = [str(col).strip() for col in df.columns]

    # Rename for consistency (adjust based on your exact headers)
    rename_map = {
        "Discipline": "discipline",
        "Scope Item": "scope_item",
        "Assumptions / Clarifications": "assumptions",
        "Exclusions": "exclusions",
        "Arup Comments": "comments",
        "Accepted": "accepted"
    }

    df = df.rename(columns=rename_map)

    # Drop empty rows
    df = df.dropna(how="all")

    # Forward fill discipline (important for your structure)
    if "discipline" in df.columns:
        df["discipline"] = df["discipline"].ffill()

    # Add ID
    df["id"] = range(1, len(df) + 1)

    # Combine text for AI / risk analysis
    df["full_text"] = (
        df["scope_item"].astype(str) + " " +
        df["assumptions"].astype(str) + " " +
        df["exclusions"].astype(str) + " " +
        df["comments"].astype(str)
    )

    return df