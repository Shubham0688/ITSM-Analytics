import pandas as pd
from src.sla_calculator import calculate_sla


def create_ticket(priority, created_at, resolved_at=None):
    return {
        "ticket_id": "TKT001",
        "created_at": created_at,
        "first_response_at": created_at,
        "resolved_at": resolved_at,
        "closed_at": resolved_at,
        "priority": priority,
        "category": "Network",
        "department": "IT",
        "agent_id": "AG001",
        "status": "Closed" if resolved_at else "Open",
        "reopened": "No",
        "escalated": "No"
    }


def test_ticket_within_sla():
    data = pd.DataFrame([
        create_ticket("Critical", "2026-01-05 09:00:00", "2026-01-05 11:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_status"] == "Within SLA"
    assert result.iloc[0]["sla_breached"] == False


def test_ticket_breached_sla():
    data = pd.DataFrame([
        create_ticket("High", "2026-01-05 09:00:00", "2026-01-05 18:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_status"] == "Breached"
    assert result.iloc[0]["sla_breached"] == True


def test_open_ticket_pending_sla():
    data = pd.DataFrame([
        create_ticket("Medium", "2026-01-05 09:00:00")
    ])
    result = calculate_sla(data, as_of="2026-01-05 10:00:00")
    assert result.iloc[0]["sla_status"] == "Pending"
    assert result.iloc[0]["sla_breached"] == False


def test_open_ticket_overdue_sla():
    data = pd.DataFrame([
        create_ticket("Critical", "2026-01-05 09:00:00")
    ])
    result = calculate_sla(data, as_of="2026-01-05 14:00:00")
    assert result.iloc[0]["sla_status"] == "Breached"
    assert result.iloc[0]["sla_breached"] == True


def test_exact_sla_deadline():
    data = pd.DataFrame([
        create_ticket("Critical", "2026-01-05 09:00:00", "2026-01-05 13:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_status"] == "Within SLA"


def test_sla_target_critical():
    data = pd.DataFrame([
        create_ticket("Critical", "2026-01-05 09:00:00", "2026-01-05 10:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_target_hours"] == 4


def test_sla_target_high():
    data = pd.DataFrame([
        create_ticket("High", "2026-01-05 09:00:00", "2026-01-05 10:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_target_hours"] == 8


def test_sla_target_medium():
    data = pd.DataFrame([
        create_ticket("Medium", "2026-01-05 09:00:00", "2026-01-05 10:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_target_hours"] == 24


def test_sla_target_low():
    data = pd.DataFrame([
        create_ticket("Low", "2026-01-05 09:00:00", "2026-01-05 10:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_target_hours"] == 48


def test_resolution_time_calculation():
    data = pd.DataFrame([
        create_ticket("High", "2026-01-05 09:00:00", "2026-01-05 12:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["resolution_time_hours"] == 3


def test_first_response_time_calculation():
    data = pd.DataFrame([
        {
            **create_ticket("High", "2026-01-05 09:00:00", "2026-01-05 12:00:00"),
            "first_response_at": "2026-01-05 10:30:00"
        }
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["first_response_time_hours"] == 1.5


def test_sla_deadline_calculation():
    data = pd.DataFrame([
        create_ticket("Medium", "2026-01-05 09:00:00", "2026-01-05 10:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["sla_deadline"] == pd.Timestamp("2026-01-06 09:00:00")


def test_weekend_hours_are_included_in_resolution_time():
    data = pd.DataFrame([
        create_ticket("High", "2026-01-10 09:00:00", "2026-01-11 09:00:00")
    ])
    result = calculate_sla(data)
    assert result.iloc[0]["resolution_time_hours"] == 24
    assert result.iloc[0]["sla_status"] == "Breached"


def test_weekend_sla_deadline_uses_calendar_hours():
    data = pd.DataFrame([
        create_ticket("Critical", "2026-01-10 09:00:00")
    ])
    result = calculate_sla(data, as_of="2026-01-10 13:00:00")
    assert result.iloc[0]["sla_deadline"] == pd.Timestamp("2026-01-10 13:00:00")
    assert result.iloc[0]["sla_status"] == "Pending"