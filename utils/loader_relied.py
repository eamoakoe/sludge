import pandas as pd

def load_relied():
    df = pd.read_excel("data/relied_info.xlsx", engine="openpyxl", header=None)

    df.columns = ["document"]

    # Clean
    df["document"] = df["document"].astype(str).str.strip()

    # Categorise
    df["category"] = df["document"].apply(classify_doc)

    # Extract location / project
    df["site"] = df["document"].apply(extract_site)

    # Detect risk signals
    df["risk_flag"] = df["document"].str.contains(
        "budgetary|estimate|proposal", case=False, na=False
    )

    return df


def classify_doc(doc):
    doc = doc.lower()

    if "pci" in doc:
        return "PCI"
    elif "proposal" in doc:
        return "Supplier Proposal"
    elif "appendix" in doc:
        return "Appendix"
    elif "batch report" in doc:
        return "Model Output"
    elif "drawing" in doc or "w wtw" in doc:
        return "Drawings"
    else:
        return "General"


def extract_site(doc):
    doc = doc.lower()

    if "wigan" in doc:
        return "Wigan"
    elif "eccles" in doc:
        return "Eccles"
    elif "salford" in doc:
        return "Salford"
    elif "davyhulme" in doc:
        return "Davyhulme"
    else:
        return "Unknown"
