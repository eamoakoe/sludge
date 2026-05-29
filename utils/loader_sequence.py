import pandas as pd


def load_sequence():
    df = pd.read_excel("data/design_sequence.xlsx", engine="openpyxl")

    df.columns = df.columns.str.lower().str.strip()

    # Expect columns like: source, target, option
    return df


def build_edges():
    # If your Excel is not structured yet, define manually
    edges = [
        ("Feasibility Scope", "Gap Analysis"),
        ("Gap Analysis", "Option 1: 40%"),
        ("Gap Analysis", "Option 2: 60%"),

        ("Option 1: 40%", "Validation Hydraulic Model"),
        ("Option 1: 40%", "Validation Mass Balance"),
        ("Option 1: 40%", "Validation Process Sizing"),

        ("Validation Hydraulic Model", "Process Block Diagram"),
        ("Validation Mass Balance", "Process Block Diagram"),
        ("Validation Process Sizing", "Process Block Diagram"),

        ("Process Block Diagram", "Agreed Process Design"),

        ("Agreed Process Design", "Mechanical Design"),
        ("Agreed Process Design", "EICA Design"),
        ("Agreed Process Design", "Civil/Structural Design"),

        ("Mechanical Design", "Basis of Design"),
        ("EICA Design", "Basis of Design"),

        ("Basis of Design", "Cost Comparison"),
        ("Cost Comparison", "Option Selection"),
        ("Option Selection", "TAG Review"),
    ]

    return edges
