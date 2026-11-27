CREATE OR REPLACE VIEW vw_ticket_sla AS
SELECT
    ticket_id,
    priority,
    category,
    status,
    department_id,
    agent_id,
    created_at,
    first_response_at,
    resolved_at,
    closed_at,
    reopened_at,
    re_resolved_at,
    reopened,
    escalated,
    CASE priority
        WHEN 'Critical' THEN 4
        WHEN 'High' THEN 8
        WHEN 'Medium' THEN 24
        WHEN 'Low' THEN 48
    END AS sla_target_hours,
    created_at + NUMTODSINTERVAL(
        CASE priority
            WHEN 'Critical' THEN 4
            WHEN 'High' THEN 8
            WHEN 'Medium' THEN 24
            WHEN 'Low' THEN 48
        END,
        'HOUR'
    ) AS sla_deadline,
    CASE
        WHEN resolved_at IS NOT NULL THEN
            ROUND(
                (CAST(resolved_at AS DATE) -
                 CAST(created_at AS DATE)) * 24,
                2
            )
        ELSE NULL
    END AS resolution_time_hours,
    CASE
        WHEN resolved_at IS NOT NULL
             AND resolved_at <= created_at + NUMTODSINTERVAL(
                 CASE priority
                     WHEN 'Critical' THEN 4
                     WHEN 'High' THEN 8
                     WHEN 'Medium' THEN 24
                     WHEN 'Low' THEN 48
                 END,
                 'HOUR'
             )
        THEN 'Within SLA'
        WHEN resolved_at IS NOT NULL THEN 'Breached'
        WHEN LOCALTIMESTAMP > created_at + NUMTODSINTERVAL(
            CASE priority
                WHEN 'Critical' THEN 4
                WHEN 'High' THEN 8
                WHEN 'Medium' THEN 24
                WHEN 'Low' THEN 48
            END,
            'HOUR'
        )
        THEN 'Breached'
        ELSE 'Pending'
    END AS sla_status
FROM tickets;