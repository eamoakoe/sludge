import pandas as pd

def load_scope(path):

    # Step 1: load raw (no header)
    df_raw = pd.read_excel(path, header=None)

    # Step 2: find real header row
    header_row = None

    for i in range(len(df_raw)):
        row = df_raw.iloc[i].astype(str).str.lower().tolist()

        # We look for BOTH key headers
        if "discipline" in row and "scope item" in row:
            header_row = i
            break

    # Step 3: reload using correct header
    if header_row is not None:
        df = pd.read_excel(path, header=header_row)
    else:
        raise ValueError("Could not find header row")

    # Step 4: clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Step 5: rename to clean format
    df = df.rename(columns={
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    })

    # Step 6: remove junk rows
    df = df[df["scope_item"].notna()]
    df = df[df["scope_item"].astype(str).str.strip() != ""]

    # Step 7: fill discipline
    df["discipline"] = df["discipline"].ffill()

    return df
