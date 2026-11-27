INSERT INTO departments (department_id, department_name)
VALUES (1, 'IT');

INSERT INTO departments (department_id, department_name)
VALUES (2, 'Application');

INSERT INTO departments (department_id, department_name)
VALUES (3, 'Security');

INSERT INTO agents (agent_id) VALUES ('AG001');
INSERT INTO agents (agent_id) VALUES ('AG002');
INSERT INTO agents (agent_id) VALUES ('AG003');
INSERT INTO agents (agent_id) VALUES ('AG004');

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG001', 1);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG001', 2);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG001', 3);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG002', 1);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG002', 2);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG002', 3);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG003', 1);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG003', 2);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG003', 3);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG004', 1);

INSERT INTO agent_departments (agent_id, department_id)
VALUES ('AG004', 3);

COMMIT;