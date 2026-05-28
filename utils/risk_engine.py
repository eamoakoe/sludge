def compute_risk(df):

    keywords = ["assume", "tbc", "to be confirmed", "supplier", "not defined"]

    def score(text):
        text = str(text).lower()
        return sum(k in text for k in keywords)

    df["risk_score"] = df["full_text"].apply(score)

    def level(x):
        if x >= 2:
            return "High"
        elif x == 1:
            return "Medium"
        else:
            return "Low"

    df["risk_level"] = df["risk_score"].apply(level)

    df["is_uncertain"] = df["full_text"].str.contains(
        "assume|tbc|to be confirmed",
        case=False,
        na=False
    )

    return df