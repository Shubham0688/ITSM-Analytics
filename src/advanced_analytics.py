import pandas as pd


def analyze_agent_performance(df):
    df = df.copy()

    df["resolved_at"] = pd.to_datetime(
        df["resolved_at"],
        errors="coerce"
    )

    df["created_at"] = pd.to_datetime(
        df["created_at"],
        errors="coerce"
    )

    df["resolution_time_hours"] = (
        df["resolved_at"] - df["created_at"]
    ).dt.total_seconds() / 3600

    resolved = df[df["resolved_at"].notna()]

    agent_report = resolved.groupby("agent_id").agg(
        tickets_resolved=("ticket_id", "count"),
        avg_resolution_hours=("resolution_time_hours", "mean"),
        sla_breaches=("sla_status", lambda x: (x == "Breached").sum()),
        reopened_tickets=("reopened", lambda x: (x == "Yes").sum())
    ).reset_index()

    agent_report["avg_resolution_hours"] = (
        agent_report["avg_resolution_hours"].round(2)
    )

    return agent_report.sort_values(
        "tickets_resolved",
        ascending=False
    )


def analyze_ticket_aging(df):
    df = df.copy()

    df["created_at"] = pd.to_datetime(
        df["created_at"],
        errors="coerce"
    )

    current_time = pd.Timestamp.now()

    pending = df[df["resolved_at"].isna()].copy()

    pending["pending_hours"] = (
        current_time - pending["created_at"]
    ).dt.total_seconds() / 3600

    pending["aging_category"] = pd.cut(
        pending["pending_hours"],
        bins=[0, 24, 48, 168, float("inf")],
        labels=["Under 24 Hours", "24-48 Hours", "2-7 Days", "Above 7 Days"]
    )

    return pending[
        [
            "ticket_id",
            "priority",
            "category",
            "department",
            "agent_id",
            "created_at",
            "pending_hours",
            "aging_category"
        ]
    ]


if __name__ == "__main__":
    data = pd.read_csv("data/cleaned_tickets.csv")

    data["resolved_at"] = pd.to_datetime(
        data["resolved_at"],
        errors="coerce"
    )

    from sla_calculator import calculate_sla

    data = calculate_sla(data)

    agent_report = analyze_agent_performance(data)
    aging_report = analyze_ticket_aging(data)

    print("\nAGENT PERFORMANCE")
    print(agent_report.to_string(index=False))

    print("\nTICKET AGING")
    print(aging_report.to_string(index=False))

    agent_report.to_csv(
        "reports/agent_performance.csv",
        index=False
    )

    aging_report.to_csv(
        "reports/ticket_aging.csv",
        index=False
    )

    print("\nReports saved successfully.")