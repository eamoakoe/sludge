import pandas as pd

def load_scope(path):

    # Load raw (handles messy Excel)
    df = pd.read_excel(path, header=None)

    # Convert to string
    df = df.astype(str)

    # Find header row
    header_row = None
    for i in range(len(df)):
        row = df.iloc[i].str.lower().tolist()
        if "discipline" in row and "scope item" in row:
            header_row = i
            break

    # Reload properly
    if header_row is not None:
        df = pd.read_excel(path, header=header_row)
    else:
        df = pd.read_excel(path, header=0)

    # Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Rename columns
    df = df.rename(columns={
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    })

    # Ensure columns exist
    for col in ["discipline", "scope_item", "assumptions", "comments"]:
        if col not in df.columns:
            df[col] = ""

    # Clean rows
    df = df[df["scope_item"].notna()]
    df = df[df["scope_item"].astype(str).str.strip() != ""]

    # Forward fill discipline
    df["discipline"] = df["discipline"].ffill()

    return df