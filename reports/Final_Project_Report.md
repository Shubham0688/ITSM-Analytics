# ITSM ANALYTICS
## Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

**HCL Career Project – Serial No. 27**

**Project Title:** IT Help-Desk Ticket Analysis  
**Enhanced Project Title:** ITSM Analytics – Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

---

## 1. Executive Summary

ITSM Analytics is a data-driven help-desk ticket analysis and SLA monitoring system designed to improve IT service management.

The project analyzes help-desk tickets to measure resolution performance, monitor Service Level Agreement (SLA) compliance, identify overdue tickets, and evaluate agent and department performance.

The solution integrates Python for data processing and analytics, Oracle SQL for relational database management, Streamlit for interactive reporting, and Power BI for business intelligence visualization.

The project uses a dataset containing 25 help-desk tickets.

## 2. Problem Statement

Organizations receive IT support requests related to hardware, software, network, server access, and security.

Managing these requests manually makes it difficult to:

- Monitor ticket resolution times.
- Identify SLA violations.
- Track pending and overdue tickets.
- Compare agent performance.
- Analyze department workloads.
- Identify frequently occurring ticket categories.

The project addresses these challenges through centralized data analysis and interactive dashboards.

## 3. Project Objectives

1. Analyze IT help-desk ticket data.
2. Calculate ticket resolution time using Python datetime operations.
3. Calculate first response time.
4. Monitor SLA compliance based on ticket priority.
5. Identify SLA-breached and pending tickets.
6. Analyze priority-wise and category-wise ticket distribution.
7. Evaluate agent and department performance.
8. Monitor ticket aging and backlog.
9. Analyze reopened and escalated tickets.
10. Present insights through interactive dashboards.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data cleaning and analytics |
| Pandas | Data manipulation |
| Oracle SQL | Relational database and queries |
| Streamlit | Interactive analytics dashboard |
| Power BI | Business intelligence visualization |
| Matplotlib / Plotting Libraries | Data visualization |
| Pytest | Automated testing |
| CSV | Dataset storage and exchange |
| VS Code | Development environment |

## 5. Dataset Description

The project uses a help-desk dataset containing 25 tickets.

Important attributes include:

- ticket_id
- created_at
- first_response_at
- resolved_at
- closed_at
- priority
- category
- department
- agent_id
- status
- reopened
- escalated

The dataset contains 21 resolved tickets and 4 unresolved tickets.

## 6. Data Cleaning and Quality Validation

Python was used to load, clean, and validate the dataset.

Data quality checks included:

- Missing ticket IDs.
- Duplicate ticket IDs.
- Invalid priority values.
- Missing creation dates.
- Invalid response and resolution dates.
- Missing departments and categories.
- Invalid reopened and escalated values.

The validation report identified zero errors in the checked fields.

The cleaned dataset contains all 25 tickets.

## 7. SLA Calculation Methodology

The project uses priority-based SLA targets.

| Priority | SLA Target |
|---|---:|
| Critical | 4 hours |
| High | 8 hours |
| Medium | 24 hours |
| Low | 48 hours |

Resolution time is calculated as:

Resolution Time = Resolved Time − Created Time

First response time is calculated as:

First Response Time = First Response Time − Created Time

SLA classification:

- Within SLA: Resolved within the target.
- Breached: Resolution exceeded the target.
- Pending: Unresolved and still within the SLA deadline.
- Overdue unresolved tickets are classified as breached.

The calculations use elapsed calendar hours, including weekends.

## 8. SQL Database Design

The Oracle database contains four main relational tables:

1. DEPARTMENTS
2. AGENTS
3. AGENT_DEPARTMENTS
4. TICKETS

SQL implementation includes:

- Database schema creation.
- Master data insertion.
- Ticket data insertion.
- SLA-related queries.
- Analytical views.
- KPI queries.
- Database indexes.

The database supports ticket analysis, SLA reporting, and agent and department performance monitoring.

## 9. Advanced Analytics

The project includes the following analytical modules:

### Agent Performance
- Tickets resolved by each agent.
- Average resolution time.
- SLA breaches.
- Reopened tickets.

### Department Analytics
- Department-wise ticket distribution.
- Workload analysis.
- SLA performance.

### Ticket Aging
- Identification of pending tickets.
- Calculation of ticket age.
- Backlog classification.

### Business Insights
- Priority distribution.
- Category distribution.
- Reopened ticket analysis.
- Escalation analysis.

## 10. Key Business Results

### Overall Performance

| Metric | Result |
|---|---:|
| Total Tickets | 25 |
| Resolved Tickets | 21 |
| Open Tickets | 4 |
| Within SLA | 5 |
| SLA Breached | 20 |
| Pending SLA | 0 |
| Overall SLA Breach | 80.00% |
| Average Resolution Time | 30.48 hours |
| Reopened Tickets | 4 |
| Escalated Tickets | 7 |

### Priority-wise Distribution

| Priority | Tickets |
|---|---:|
| Critical | 7 |
| High | 7 |
| Medium | 6 |
| Low | 5 |

### Category-wise Distribution

| Category | Tickets |
|---|---:|
| Hardware | 5 |
| Network | 5 |
| Software | 5 |
| Access | 4 |
| Server | 4 |
| Security | 2 |

### Additional SLA Insight

Out of 21 resolved tickets:

- 5 were resolved within SLA.
- 16 breached their SLA.
- Resolved-ticket SLA breach percentage was 76.19%.

The overall SLA breach percentage is 80%, because it also includes four overdue unresolved tickets.

## 11. Interactive Dashboards

### Streamlit Dashboard

The Streamlit dashboard provides:

- Executive Dashboard.
- SLA Performance.
- Department Analytics.
- Agent Performance Analysis.
- Ticket Aging Analysis.
- Business Insights.
- CSV export functionality.

### Power BI Dashboard

The Power BI report includes:

- Ticket KPI cards.
- Resolution and SLA metrics.
- Priority-wise ticket analysis.
- Category-wise ticket analysis.

The Power BI report is saved separately in the project's powerbi folder.

## 12. Automated Testing

Pytest was used to validate SLA calculation functionality.

The automated test cases cover:

- Within-SLA tickets.
- Breached tickets.
- Pending tickets.
- Overdue open tickets.
- Exact SLA deadline conditions.
- Priority-based SLA targets.
- Resolution time.
- First response time.
- SLA deadline calculations.
- Weekend handling.

**Testing Result: 14 tests passed successfully.**

## 13. Manual Verification

An independent Python datetime-based verification process was performed on all 25 tickets.

The calculated results were compared with the project's SLA calculation output.

All 25 ticket records passed the automated independent verification checks.

This is an independent calculation-based verification, not a human audit.

## 14. Database Performance Considerations

Database indexes were created on selected ticket columns, including:

- Creation date.
- Resolution date.
- Department.
- Agent.
- Reopening timestamp.

These indexes are intended to support frequently used filtering and analytical queries. No measured query performance improvement is claimed.

## 15. Limitations

1. The project currently uses a relatively small dataset of 25 tickets.
2. The SLA model uses calendar hours rather than business hours.
3. Four tickets remain unresolved and are overdue according to the analysis date.
4. Reopened ticket timestamps are missing for the four reopened records.
5. Actual second-cycle resolution time cannot be calculated without reopening timestamps.
6. The star schema is documented as a proposed analytical model, while the implemented Oracle database uses normalized relational tables.
7. The dashboard is an analytical prototype and does not represent a fully integrated enterprise ITSM production platform.

## 16. Future Scope

Potential future improvements include:

- Integration with live ITSM ticketing systems.
- Larger real-world datasets.
- Business-hours-based SLA calculations.
- Automated ticket assignment.
- Predictive SLA breach alerts.
- Machine learning-based ticket classification.
- Root-cause analysis.
- Real-time monitoring.
- Complete reopened-ticket lifecycle tracking.
- Role-based access and authentication.

## 17. Conclusion

ITSM Analytics successfully demonstrates how Python, Oracle SQL, Streamlit, and Power BI can be combined to analyze IT help-desk operations.

The project provides measurable insights into ticket resolution, SLA compliance, ticket aging, agent performance, department workload, and ticket categories.

The implementation includes data cleaning, analytical processing, SQL database management, automated testing, independent verification, and interactive dashboards.

The project demonstrates a practical foundation for data-driven IT service management and continuous service improvement.

---

**Project:** ITSM Analytics – Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

**Project Reference:** HCL Career – Project Serial No. 27