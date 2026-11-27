import pandas as pd

VALID_PRIORITIES = ["Critical", "High", "Medium", "Low"]
VALID_FLAGS = ["Yes", "No"]


def validate_ticket_data(df):
    if df is None or df.empty:
        raise ValueError("Ticket dataset is empty.")

    df = df.copy()

    date_columns = [
        "created_at",
        "first_response_at",
        "resolved_at",
        "closed_at"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    results = {
        "Total Tickets": len(df),
        "Missing Ticket IDs": df["ticket_id"].isna().sum(),
        "Duplicate Ticket IDs": df["ticket_id"].duplicated().sum(),
        "Invalid Priorities": (~df["priority"].isin(VALID_PRIORITIES)).sum(),
        "Missing Created Dates": df["created_at"].isna().sum(),
        "Invalid First Response Dates": (
            df["first_response_at"].notna()
            & (df["first_response_at"] < df["created_at"])
        ).sum(),
        "Invalid Resolution Dates": (
            df["resolved_at"].notna()
            & (df["resolved_at"] < df["created_at"])
        ).sum(),
        "Invalid Closing Dates": (
            df["closed_at"].notna()
            & (df["resolved_at"].notna())
            & (df["closed_at"] < df["resolved_at"])
        ).sum(),
        "Missing Departments": df["department"].isna().sum(),
        "Missing Categories": df["category"].isna().sum(),
        "Invalid Reopened Values": (~df["reopened"].isin(VALID_FLAGS)).sum(),
        "Invalid Escalated Values": (~df["escalated"].isin(VALID_FLAGS)).sum()
    }

    report = pd.DataFrame(
        list(results.items()),
        columns=["Quality Check", "Count"]
    )

    return report


if __name__ == "__main__":
    data = pd.read_csv("data/cleaned_tickets.csv")

    report = validate_ticket_data(data)

    print("\nITSM DATA QUALITY REPORT")
    print(report.to_string(index=False))

    report.to_csv("reports/data_quality_report.csv", index=False)

    print("\nData quality report saved successfully.")