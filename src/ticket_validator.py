import pandas as pd

REQUIRED_COLUMNS = [
    "ticket_id",
    "created_at",
    "priority",
    "category",
    "department",
    "agent_id",
    "status",
    "reopened",
    "escalated"
]

DATE_COLUMNS = [
    "created_at",
    "first_response_at",
    "resolved_at",
    "closed_at"
]

VALID_PRIORITIES = [
    "Critical",
    "High",
    "Medium",
    "Low"
]

VALID_FLAGS = ["Yes", "No"]


def validate_ticket_data(df):
    df = df.copy()
    issues = []

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    invalid_rows = set()

    for column in REQUIRED_COLUMNS:
        missing = df[column].isna() | (
            df[column].astype(str).str.strip() == ""
        )

        for index in df.index[missing]:
            issues.append({
                "row": index + 2,
                "column": column,
                "issue": "Missing required value"
            })
            invalid_rows.add(index)

    duplicates = df["ticket_id"].duplicated(keep=False)

    for index in df.index[duplicates]:
        issues.append({
            "row": index + 2,
            "column": "ticket_id",
            "issue": "Duplicate ticket ID"
        })
        invalid_rows.add(index)

    for column in DATE_COLUMNS:
        if column in df.columns:
            original = df[column].copy()
            parsed = pd.to_datetime(original, errors="coerce")

            invalid_dates = original.notna() & parsed.isna()

            for index in df.index[invalid_dates]:
                issues.append({
                    "row": index + 2,
                    "column": column,
                    "issue": "Invalid date value"
                })
                invalid_rows.add(index)

            df[column] = parsed

    invalid_priority = ~df["priority"].isin(VALID_PRIORITIES)

    for index in df.index[invalid_priority]:
        issues.append({
            "row": index + 2,
            "column": "priority",
            "issue": "Invalid priority"
        })
        invalid_rows.add(index)

    for column in ["reopened", "escalated"]:
        invalid_flags = ~df[column].isin(VALID_FLAGS)

        for index in df.index[invalid_flags]:
            issues.append({
                "row": index + 2,
                "column": column,
                "issue": "Expected Yes or No"
            })
            invalid_rows.add(index)

    valid_df = df.drop(index=list(invalid_rows)).copy()
    issues_df = pd.DataFrame(
        issues,
        columns=["row", "column", "issue"]
    )

    return valid_df, issues_df