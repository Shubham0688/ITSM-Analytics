CREATE INDEX idx_tickets_created_at
ON tickets(created_at);

CREATE INDEX idx_tickets_resolved_at
ON tickets(resolved_at);

CREATE INDEX idx_tickets_department
ON tickets(department_id);

CREATE INDEX idx_tickets_agent
ON tickets(agent_id);

CREATE INDEX idx_tickets_reopened_at
ON tickets(reopened_at);