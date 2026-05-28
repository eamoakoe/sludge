import pandas as pd

def load_scope(path):

    # ✅ Load raw Excel (no assumptions)
    df = pd.read_excel(path, header=None)

    # ✅ Convert everything to string
    df = df.astype(str)

    # ✅ Find header row (where Discipline appears)
    header_row = None

    for i in range(len(df)):
        row = df.iloc[i].str.lower().tolist()
        if "discipline" in row and "scope item" in row:
            header_row = i
            break

    # ✅ Reload with correct header
    if header_row is not None:
        df = pd.read_excel(path, header=header_row)
    else:
        # fallback
        df = pd.read_excel(path, header=0)

    # ✅ Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # ✅ Rename
    df = df.rename(columns={
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    })

    # ✅ Remove junk rows (critical)
    df = df[df["scope_item"].notna()]
    df = df[df["scope_item"].str.strip() != ""]

    # ✅ Forward fill discipline
    df["discipline"] = df["discipline"].ffill()

    # ✅ Clean text
    df["scope_item"] = df["scope_item"].astype(str)
    df["assumptions"] = df.get("assumptions", "").astype(str)
    df["comments"] = df.get("comments", "").astype(str)

    return df
