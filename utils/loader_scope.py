import pandas as pd

def load_scope(path):

    # ✅ Load file (your header is already correct row)
    df = pd.read_excel(path)

    # ✅ Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # ✅ Rename columns properly
    df = df.rename(columns={
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments"
    })

    # ✅ Ensure required columns exist
    for col in ["discipline", "scope_item", "assumptions", "comments"]:
        if col not in df.columns:
            df[col] = ""

    # ✅ Convert everything to string
    df = df.astype(str)

    # ✅ Remove empty rows
    df = df[df["scope_item"].str.strip() != ""]
    df = df[df["scope_item"].str.lower() != "nan"]

    # ✅ Forward fill discipline (VERY IMPORTANT for your file)
    df["discipline"] = df["discipline"].replace("nan", "")
    df["discipline"] = df["discipline"].replace("", None)
    df["discipline"] = df["discipline"].ffill()

    # ✅ Remove section headers (non-real disciplines)
    invalid_disciplines = [
        "technical governance and assurance",
        "40% option - amp9 requirements",
        "60% option - amp10 storm spill requirements",
        "optimised 60% option - amp10 storm spill requirements",
        "general / other",
        "temporary works"
    ]

    df = df[
        ~df["discipline"].str.lower().isin(invalid_disciplines)
    ]

    # ✅ Clean discipline labels
    df["discipline"] = df["discipline"].str.strip()

    # ✅ Create full_text (safe for future features)
    df["full_text"] = (
        df["scope_item"] + " " +
        df["assumptions"] + " " +
        df["comments"]
    )

    return df