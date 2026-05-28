import pandas as pd

def load_scope(path):

    # Load raw
    df_raw = pd.read_excel(path, header=None)

    header_row = None

    # Find real header row (flexible)
    for i in range(len(df_raw)):
        row = df_raw.iloc[i].astype(str).str.lower()

        if (
            row.str.contains("discipline").any() and
            row.str.contains("scope").any()
        ):
            header_row = i
            break

    # Reload using detected header
    if header_row is not None:
        df = pd.read_excel(path, header=header_row)
    else:
        df = pd.read_excel(path, header=1)

    # Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Rename IMPORTANT columns
    df = df.rename(columns={
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "arup comments": "comments"
    })

    # ✅ FORCE columns to exist (this fixes your error)
    if "discipline" not in df.columns:
        df["discipline"] = "Unknown"

    if "scope_item" not in df.columns:
        # Try to recover from generic columns
        df["scope_item"] = df.iloc[:, 1].astype(str)

    if "assumptions" not in df.columns:
        df["assumptions"] = ""

    if "comments" not in df.columns:
        df["comments"] = ""

    # ✅ Clean rows
    df = df[df["scope_item"].astype(str).str.strip() != ""]

    # ✅ Forward fill discipline
    df["discipline"] = df["discipline"].replace("nan", None)
    df["discipline"] = df["discipline"].ffill()

    # ✅ Final fallback (avoid blank discipline)
    df["discipline"] = df["discipline"].fillna("Unknown")

    return df