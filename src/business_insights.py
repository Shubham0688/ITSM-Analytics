import pandas as pd
from sla_calculator import calculate_sla


def generate_business_insights(df):
    df = calculate_sla(df)

    total_tickets = len(df)

    resolved = df[df["resolved_at"].notna()]
    open_tickets = df["resolved_at"].isna().sum()

    within_sla = (df["sla_status"] == "Within SLA").sum()
    total_breached = (df["sla_status"] == "Breached").sum()
    pending_sla = (df["sla_status"] == "Pending").sum()

    resolved_breached = (
        resolved["sla_status"] == "Breached"
    ).sum()

    overall_breach_percentage = (
        total_breached / total_tickets * 100
        if total_tickets > 0 else 0
    )

    resolved_breach_percentage = (
        resolved_breached / len(resolved) * 100
        if len(resolved) > 0 else 0
    )

    priority_report = df.groupby("priority").size().sort_values(
        ascending=False
    )

    category_report = df.groupby("category").size().sort_values(
        ascending=False
    )

    reopened = (df["reopened"] == "Yes").sum()
    escalated = (df["escalated"] == "Yes").sum()

    insights = [
        "ITSM BUSINESS INSIGHTS REPORT",
        "=" * 45,
        f"Total Tickets: {total_tickets}",
        f"Resolved Tickets: {len(resolved)}",
        f"Open Tickets: {open_tickets}",
        f"Tickets Within SLA: {within_sla}",
        f"Tickets Breaching SLA: {total_breached}",
        f"Tickets with Pending SLA: {pending_sla}",
        f"Overall SLA Breach Percentage: {overall_breach_percentage:.2f}%",
        f"Resolved Ticket SLA Breaches: {resolved_breached}",
        f"Resolved Ticket SLA Breach Percentage: {resolved_breach_percentage:.2f}%",
        f"Reopened Tickets: {reopened}",
        f"Escalated Tickets: {escalated}",
        "",
        "TICKETS BY PRIORITY",
        "-" * 30,
        priority_report.to_string(),
        "",
        "TICKETS BY CATEGORY",
        "-" * 30,
        category_report.to_string()
    ]

    return "\n".join(insights)


if __name__ == "__main__":
    data = pd.read_csv("data/cleaned_tickets.csv")

    report = generate_business_insights(data)

    print(report)

    with open("reports/business_insights.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("\nBusiness insights report saved successfully.")