WITH ticket_sla AS (
    SELECT
        ticket_id,
        priority,
        created_at,
        first_response_at,
        resolved_at,
        closed_at,
        CASE priority
            WHEN 'Critical' THEN 4
            WHEN 'High' THEN 8
            WHEN 'Medium' THEN 24
            WHEN 'Low' THEN 48
        END AS sla_target_hours
    FROM tickets
)
SELECT
    ticket_id,
    priority,
    created_at,
    first_response_at,
    resolved_at,
    sla_target_hours,
    created_at + NUMTODSINTERVAL(sla_target_hours, 'HOUR') AS sla_deadline,
    CASE
        WHEN resolved_at IS NOT NULL THEN
            ROUND(
                (CAST(resolved_at AS DATE) - CAST(created_at AS DATE)) * 24,
                2
            )
        ELSE NULL
    END AS resolution_time_hours,
    CASE
        WHEN resolved_at IS NOT NULL
             AND resolved_at <= created_at + NUMTODSINTERVAL(sla_target_hours, 'HOUR')
        THEN 'Within SLA'
        WHEN resolved_at IS NOT NULL THEN 'Breached'
        WHEN LOCALTIMESTAMP > created_at + NUMTODSINTERVAL(sla_target_hours, 'HOUR')
        THEN 'Breached'
        ELSE 'Pending'
    END AS sla_status
FROM ticket_sla;