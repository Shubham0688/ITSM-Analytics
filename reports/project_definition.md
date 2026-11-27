# ITSM Analytics – Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

## 1. Problem Statement

IT help-desk teams receive support requests related to hardware, software, networks, access, and other IT services.

Without proper monitoring and analysis, organizations may struggle to identify delayed tickets, SLA violations, repeated issues, agent workload, and unresolved backlogs.

ITSM Analytics addresses this problem by developing a data-driven ticket analysis and SLA monitoring system using Python, Oracle SQL, and Power BI.

The system processes help-desk ticket data, calculates resolution and response times, identifies SLA breaches, evaluates operational performance, and presents meaningful insights through interactive dashboards.

## 2. Project Objectives

- Clean and validate help-desk ticket data.
- Calculate ticket resolution time using Python datetime operations.
- Calculate first-response time.
- Monitor priority-based SLA compliance.
- Identify breached and unresolved tickets.
- Analyze reopened and escalated tickets.
- Evaluate agent and department performance.
- Monitor ticket aging and backlog.
- Analyze ticket distribution by priority and category.
- Validate analytical results across Python, Oracle SQL, and Power BI.
- Generate business insights for better IT service management.

## 3. Dataset Description

The current project dataset contains 25 sample help-desk tickets.

Important fields include:

| Column | Description |
|---|---|
| ticket_id | Unique ticket identifier |
| created_at | Ticket creation timestamp |
| first_response_at | First response timestamp |
| resolved_at | Resolution timestamp |
| closed_at | Ticket closure timestamp |
| priority | Critical, High, Medium, Low |
| category | Ticket category |
| department | Responsible department |
| agent_id | Assigned support agent |
| status | Current ticket status |
| reopened | Whether the ticket was reopened |
| escalated | Whether the ticket was escalated |

The sample dataset is used for project development and validation. It does not represent real organizational records.

## 4. SLA Definitions

The project uses the following configurable example SLA targets:

| Priority | SLA Target |
|---|---:|
| Critical | 4 Hours |
| High | 8 Hours |
| Medium | 24 Hours |
| Low | 48 Hours |

These targets are project assumptions and must not be interpreted as official company policies.

The current implementation measures elapsed calendar hours. Business-hours-only SLA calculations would require a separate documented rule.

## 5. Key Performance Indicators

### 5.1 Total Tickets

Total number of unique help-desk tickets in the selected dataset.

### 5.2 Average Resolution Time

Formula:

Average Resolution Time = Sum of Resolution Time for Resolved Tickets / Number of Resolved Tickets

Only tickets with a valid resolution timestamp are included.

### 5.3 SLA Breach Percentage

Formula:

SLA Breach Percentage = (Number of Resolved Tickets Breaching SLA / Total Resolved Tickets) × 100

Unresolved tickets are excluded from this denominator and reported separately.

### 5.4 SLA Compliance Percentage

Formula:

SLA Compliance Percentage = (Resolved Tickets Within SLA / Total Resolved Tickets) × 100

### 5.5 First Response Time

First Response Time = First Response Timestamp - Ticket Creation Timestamp

### 5.6 Reopen Rate

Reopen Rate = (Number of Reopened Tickets / Total Tickets) × 100

### 5.7 Escalation Rate

Escalation Rate = (Number of Escalated Tickets / Total Tickets) × 100

### 5.8 Open Tickets

Number of tickets that have not yet been resolved.

### 5.9 Ticket Aging

Measures the elapsed time between ticket creation and the current reporting time for unresolved tickets.

### 5.10 Agent Performance

Evaluates agents using resolved ticket count, average resolution time, SLA breaches, and reopened tickets.

## 6. Data Validation Rules

The project will validate:

- Missing ticket identifiers.
- Duplicate ticket identifiers.
- Invalid priority values.
- Missing creation timestamps.
- Invalid response timestamps.
- Invalid resolution timestamps.
- Invalid closing timestamps.
- Missing departments and categories.
- Invalid reopened and escalation flags.
- Tickets without resolution or closing timestamps.
- Reopened ticket scenarios.
- Weekend ticket scenarios.

## 7. Acceptance Criteria

The project will be considered technically validated when:

1. Resolution time calculations match manual verification for at least 20 tickets.
2. SLA breach percentage matches independently calculated results.
3. Average resolution time matches independently calculated results.
4. Reopened ticket cases are tested.
5. Tickets without closing timestamps are handled correctly.
6. Weekend scenarios are tested and documented.
7. Tickets are correctly grouped by priority and category.
8. Python and Oracle SQL analytical results reconcile.
9. Power BI dashboard displays validated KPIs.
10. Dashboard slicers and drill-downs work correctly.
11. Automated tests pass.
12. Data-quality findings are documented.

## 8. Expected Deliverables

- Problem statement and KPI definitions.
- ER diagram or star-schema diagram.
- Python data cleaning and analytical scripts.
- Oracle SQL scripts for DDL, data loading, queries, and views.
- Power BI SLA dashboard with slicers and drill-down.
- Data-quality report.
- Business insights summary.
- README documentation.
- GitHub repository.
- Project demonstration video.

## 9. Project Limitations

- Current dataset is a sample dataset containing 25 tickets.
- SLA targets are configurable assumptions.
- Current SLA calculations use elapsed calendar hours.
- Oracle database integration and Power BI implementation require separate execution and validation.

## 10. Project Goal

To transform raw IT help-desk ticket records into reliable operational insights that support SLA monitoring, backlog management, service quality analysis, and data-driven decision-making.