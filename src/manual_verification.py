import pandas as pd
from datetime import datetime
from pathlib import Path
from sla_calculator import calculate_sla


SLA_TARGETS = {
    "Critical": 4,
    "High": 8,
    "Medium": 24,
    "Low": 48
}


def parse_datetime(value):
    if pd.isna(value):
        return None
    return datetime.fromisoformat(str(value))


def create_manual_verification():
    data = pd.read_csv("data/cleaned_tickets.csv")

    as_of = datetime.now()

    result = calculate_sla(data, as_of=as_of)

    manual_hours = []
    expected_statuses = []

    for _, row in result.iterrows():
        created_at = parse_datetime(row["created_at"])
        resolved_at = parse_datetime(row["resolved_at"])

        target = SLA_TARGETS[row["priority"]]

        if resolved_at is not None:
            hours = (
                resolved_at - created_at
            ).total_seconds() / 3600

            expected_status = (
                "Within SLA" if hours <= target else "Breached"
            )
        else:
            hours = None

            deadline = (
                created_at.timestamp() + target * 3600
            )

            expected_status = (
                "Breached"
                if as_of.timestamp() > deadline
                else "Pending"
            )

        manual_hours.append(hours)
        expected_statuses.append(expected_status)

    result["manual_resolution_hours"] = manual_hours
    result["manual_expected_status"] = expected_statuses

    result["manual_verification"] = (
        result["manual_expected_status"] == result["sla_status"]
    ).map({True: "PASS", False: "FAIL"})

    verification = result[[
        "ticket_id",
        "priority",
        "created_at",
        "resolved_at",
        "resolution_time_hours",
        "manual_resolution_hours",
        "sla_target_hours",
        "manual_expected_status",
        "sla_status",
        "manual_verification"
    ]]

    Path("reports").mkdir(exist_ok=True)

    verification.to_csv(
        "reports/manual_verification.csv",
        index=False
    )

    print("\n25-TICKET INDEPENDENT VERIFICATION REPORT")
    print(verification.to_string(index=False))

    print("\nVERIFICATION SUMMARY")
    print(verification["manual_verification"].value_counts())

    print("\nReport saved: reports/manual_verification.csv")


if __name__ == "__main__":
    create_manual_verification()