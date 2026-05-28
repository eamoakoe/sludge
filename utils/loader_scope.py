import pandas as pd

def load_scope(path):

    # ✅ Force raw load (no assumptions about headers)
    df = pd.read_excel(path, header=None)

    # ✅ Show raw structure (for debugging)
    print("RAW DATA PREVIEW:")
    print(df.head(10))

    # ✅ Find the real header row (where 'Discipline' appears)
    header_row = None

    for i in range(len(df)):
        row_values = df.iloc[i].astype(str).str.lower().tolist()
        if "discipline" in row_values:
            header_row = i
            break

    # ✅ If header found → reload correctly
    if header_row is not None:
        df = pd.read_excel(path, header=header_row)
    else:
        # fallback: assume row 0
        df = pd.read_excel(path, header=0)

    # ✅ Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # ✅ Rename columns
    rename_map = {
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    }

    df = df.rename(columns=rename_map)

    # ✅ Ensure columns exist
    for col in ["discipline", "scope_item", "assumptions", "comments"]:
        if col not in df.columns:
            df[col] = ""

    # ✅ Forward fill discipline
    df["discipline"] = df["discipline"].ffill()

    # ✅ Remove empty rows
    df = df[df["scope_item"].notna()]

    # ✅ Add ID
    df["id"] = range(1, len(df) + 1)

    # ✅ Combine text
    df["full_text"] = (
        df["scope_item"].astype(str) + " " +
        df["assumptions"].astype(str) + " " +
        df["comments"].astype(str)
    )

    return df
