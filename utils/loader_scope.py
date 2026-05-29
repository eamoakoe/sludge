import pandas as pd

def load_scope(path):

    # Load raw
    df = pd.read_excel(path, header=0)

    # Clean column names
    df.columns = [str(col).strip().lower() for col in df.columns]

    # Rename properly
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

    # ✅ Clean strings
    df = df.astype(str)

    # ✅ Remove empty scope rows
    df = df[df["scope_item"].str.strip() != ""]
    df = df[df["scope_item"].str.lower() != "nan"]

    # ✅ Forward fill discipline
    df["discipline"] = df["discipline"].replace("nan", None)
    df["discipline"] = df["discipline"].ffill()

    # ✅ REMOVE section headers (critical for your file)
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

    # ✅ Final clean
    df["discipline"] = df["discipline"].str.strip()

    return df
