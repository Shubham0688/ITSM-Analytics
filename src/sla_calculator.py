import pandas as pd

SLA_TARGETS = {
    "Critical": 4,
    "High": 8,
    "Medium": 24,
    "Low": 48
}


def calculate_sla(df, as_of=None):
    df = df.copy()

    date_columns = [
        "created_at",
        "first_response_at",
        "resolved_at",
        "closed_at"
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    if as_of is None:
        as_of = pd.Timestamp.now()
    else:
        as_of = pd.Timestamp(as_of)

    df["sla_target_hours"] = df["priority"].map(SLA_TARGETS)

    df["resolution_time_hours"] = (
        df["resolved_at"] - df["created_at"]
    ).dt.total_seconds() / 3600

    df["first_response_time_hours"] = (
        df["first_response_at"] - df["created_at"]
    ).dt.total_seconds() / 3600

    df["sla_deadline"] = (
        df["created_at"]
        + pd.to_timedelta(df["sla_target_hours"], unit="h")
    )

    df["sla_status"] = "Pending"

    resolved = df["resolved_at"].notna()

    df.loc[
        resolved & (
            df["resolution_time_hours"] <= df["sla_target_hours"]
        ),
        "sla_status"
    ] = "Within SLA"

    df.loc[
        resolved & (
            df["resolution_time_hours"] > df["sla_target_hours"]
        ),
        "sla_status"
    ] = "Breached"

    overdue_open = (
        ~resolved
        & df["sla_deadline"].notna()
        & (as_of > df["sla_deadline"])
    )

    df.loc[overdue_open, "sla_status"] = "Breached"

    df["sla_breached"] = df["sla_status"].eq("Breached")

    return df


if __name__ == "__main__":
    data = pd.read_csv("data/raw_tickets.csv")
    result = calculate_sla(data)

    print(result[[
        "ticket_id",
        "status",
        "resolution_time_hours",
        "sla_target_hours",
        "sla_deadline",
        "sla_status",
        "sla_breached"
    ]].to_string(index=False))