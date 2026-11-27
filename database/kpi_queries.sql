SELECT
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours
FROM vw_ticket_sla
WHERE resolution_time_hours IS NOT NULL;


SELECT
    COUNT(*) AS total_tickets,
    COUNT(CASE WHEN sla_status = 'Breached' THEN 1 END) AS breached_tickets,
    COUNT(CASE WHEN sla_status = 'Within SLA' THEN 1 END) AS within_sla_tickets,
    COUNT(CASE WHEN sla_status = 'Pending' THEN 1 END) AS pending_tickets,
    ROUND(
        COUNT(CASE WHEN sla_status = 'Breached' THEN 1 END) * 100
        / NULLIF(COUNT(*), 0),
        2
    ) AS overall_sla_breach_percentage
FROM vw_ticket_sla;


SELECT
    COUNT(*) AS resolved_tickets,
    COUNT(CASE WHEN sla_status = 'Breached' THEN 1 END) AS breached_tickets,
    COUNT(CASE WHEN sla_status = 'Within SLA' THEN 1 END) AS within_sla_tickets,
    ROUND(
        COUNT(CASE WHEN sla_status = 'Breached' THEN 1 END) * 100
        / NULLIF(COUNT(*), 0),
        2
    ) AS resolved_sla_breach_percentage
FROM vw_ticket_sla
WHERE resolved_at IS NOT NULL;


SELECT
    priority,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY priority
ORDER BY
    CASE priority
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
    END;


SELECT
    category,
    COUNT(*) AS total_tickets
FROM tickets
GROUP BY category
ORDER BY total_tickets DESC;


SELECT
    COUNT(*) AS total_tickets,
    COUNT(CASE WHEN reopened = 'Yes' THEN 1 END) AS reopened_tickets,
    ROUND(
        COUNT(CASE WHEN reopened = 'Yes' THEN 1 END) * 100
        / NULLIF(COUNT(*), 0),
        2
    ) AS reopen_percentage
FROM tickets;


SELECT
    COUNT(*) AS total_tickets,
    COUNT(CASE WHEN escalated = 'Yes' THEN 1 END) AS escalated_tickets,
    ROUND(
        COUNT(CASE WHEN escalated = 'Yes' THEN 1 END) * 100
        / NULLIF(COUNT(*), 0),
        2
    ) AS escalation_percentage
FROM tickets;
SELECT
    agent_id,
    COUNT(CASE WHEN resolved_at IS NOT NULL THEN 1 END) AS tickets_resolved,
    ROUND(
        AVG(
            CASE
                WHEN resolved_at IS NOT NULL
                THEN resolution_time_hours
            END
        ),
        2
    ) AS avg_resolution_hours,
    COUNT(
        CASE
            WHEN resolved_at IS NOT NULL
                 AND sla_status = 'Breached'
            THEN 1
        END
    ) AS sla_breaches,
    COUNT(
        CASE
            WHEN reopened = 'Yes'
                 AND resolved_at IS NOT NULL
            THEN 1
        END
    ) AS reopened_tickets
FROM vw_ticket_sla
GROUP BY agent_id
ORDER BY tickets_resolved DESC;
SELECT
    d.department_name,
    COUNT(v.ticket_id) AS total_tickets,
    COUNT(
        CASE WHEN v.resolved_at IS NOT NULL THEN 1 END
    ) AS resolved_tickets,
    COUNT(
        CASE WHEN v.sla_status = 'Breached' THEN 1 END
    ) AS sla_breaches,
    ROUND(
        AVG(v.resolution_time_hours),
        2
    ) AS avg_resolution_hours
FROM departments d
LEFT JOIN vw_ticket_sla v
    ON d.department_id = v.department_id
GROUP BY d.department_name
ORDER BY total_tickets DESC;
SELECT
    ticket_id,
    priority,
    category,
    department_id,
    agent_id,
    created_at,
    ROUND(
        (CAST(LOCALTIMESTAMP AS DATE) - CAST(created_at AS DATE)) * 24,
        2
    ) AS pending_hours,
    CASE
        WHEN (CAST(LOCALTIMESTAMP AS DATE) - CAST(created_at AS DATE)) * 24 <= 24
        THEN 'Within 24 Hours'
        WHEN (CAST(LOCALTIMESTAMP AS DATE) - CAST(created_at AS DATE)) * 24 <= 72
        THEN '1-3 Days'
        WHEN (CAST(LOCALTIMESTAMP AS DATE) - CAST(created_at AS DATE)) * 24 <= 168
        THEN '3-7 Days'
        ELSE 'Above 7 Days'
    END AS aging_bucket
FROM vw_ticket_sla
WHERE resolved_at IS NULL
ORDER BY pending_hours DESC;
SELECT
    COUNT(*) AS total_reopened_tickets,
    COUNT(
        CASE WHEN reopened_at IS NOT NULL THEN 1 END
    ) AS tickets_with_reopen_timestamp,
    COUNT(
        CASE WHEN re_resolved_at IS NOT NULL THEN 1 END
    ) AS tickets_resolved_again,
    COUNT(
        CASE
            WHEN reopened = 'Yes'
                 AND reopened_at IS NULL
            THEN 1
        END
    ) AS missing_reopen_timestamps,
    ROUND(
        AVG(
            CASE
                WHEN reopened_at IS NOT NULL
                     AND re_resolved_at IS NOT NULL
                THEN
                    (CAST(re_resolved_at AS DATE) -
                     CAST(reopened_at AS DATE)) * 24
            END
        ),
        2
    ) AS avg_reopen_resolution_hours
FROM tickets
WHERE reopened = 'Yes';