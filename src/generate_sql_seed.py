import pandas as pd
from pathlib import Path

df = pd.read_csv("data/cleaned_tickets.csv")

department_ids = {
    "IT": 1,
    "Application": 2,
    "Security": 3
}

columns = [
    "ticket_id",
    "created_at",
    "first_response_at",
    "resolved_at",
    "closed_at",
    "reopened_at",
    "re_resolved_at",
    "priority",
    "category",
    "department_id",
    "agent_id",
    "status",
    "reopened",
    "escalated"
]


def sql_value(value, is_date=False):
    if pd.isna(value):
        return "NULL"

    if is_date:
        timestamp = pd.to_datetime(value)
        formatted = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"TO_TIMESTAMP('{formatted}', 'YYYY-MM-DD HH24:MI:SS')"

    if isinstance(value, str):
        return "'" + value.replace("'", "''") + "'"

    return str(value)


statements = []

for _, row in df.iterrows():
    values = [
        sql_value(row["ticket_id"]),
        sql_value(row["created_at"], True),
        sql_value(row["first_response_at"], True),
        sql_value(row["resolved_at"], True),
        sql_value(row["closed_at"], True),
        "NULL",
        "NULL",
        sql_value(row["priority"]),
        sql_value(row["category"]),
        str(department_ids[row["department"]]),
        sql_value(row["agent_id"]),
        sql_value(row["status"]),
        sql_value(row["reopened"]),
        sql_value(row["escalated"])
    ]

    statement = (
        f"INSERT INTO tickets ({', '.join(columns)}) "
        f"VALUES ({', '.join(values)});"
    )

    statements.append(statement)

output = Path("database/insert_tickets.sql")
output.write_text("\n\n".join(statements) + "\nCOMMIT;\n", encoding="utf-8")

print(f"Generated {len(statements)} ticket INSERT statements.")
print(f"Output: {output}")