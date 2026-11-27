# ITSM ANALYTICS
## Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

**HCL Career Project – Serial No. 27**

**Project Title:** IT Help-Desk Ticket Analysis  
**Enhanced Project Title:** ITSM Analytics – Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

---

## 1. Executive Summary

ITSM Analytics is a data-driven help-desk ticket analysis and SLA monitoring system designed to improve IT service management.

The project analyzes help-desk tickets to measure resolution performance, monitor Service Level Agreement (SLA) compliance, identify overdue tickets, and evaluate agent and department performance.

The solution combines Python for data processing and analytics, Oracle SQL for relational database management, Streamlit for interactive reporting, and Power BI for business intelligence visualization.

The system also supports CSV-based ticket uploads with automated data validation, allowing users to analyze help-desk exports without manually modifying the source dataset.

The project uses a sample dataset containing 25 help-desk tickets.

## 2. Problem Statement

Organizations receive IT support requests related to hardware, software, network, server access, and security.

Managing these requests manually makes it difficult to:

- Monitor ticket resolution times.
- Identify SLA violations.
- Track pending and overdue tickets.
- Compare agent performance.
- Analyze department workloads.
- Identify frequently occurring ticket categories.

The project addresses these challenges through centralized data analysis, automated SLA calculations, and interactive dashboards.

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
10. Validate uploaded ticket datasets.
11. Present insights through interactive dashboards.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data cleaning and analytics |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Interactive analytics dashboard |
| Oracle SQL | Relational database and analytical queries |
| Power BI | Business intelligence visualization |
| Pytest | Automated testing |
| CSV | Dataset storage and exchange |
| Git & GitHub | Version control |
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

The dataset contains:

- 25 total tickets.
- 21 resolved tickets.
- 4 unresolved tickets.

The dataset is used for project demonstration and does not represent actual HCL organizational data.

## 6. Data Cleaning and Quality Validation

Python and Pandas were used to load, clean, process, and validate the dataset.

The data quality process includes:

- Required field validation.
- Missing required value detection.
- Duplicate ticket ID detection.
- Invalid date value detection.
- Invalid priority validation.
- Invalid reopened and escalation flag validation.

The CSV upload validation module reports records containing validation issues separately from valid records.

The current sample dataset contains 25 valid tickets with zero reported validation issues.

## 7. SLA Calculation Methodology

The project uses priority-based SLA targets.

| Priority | SLA Target |
|---|---:|
| Critical | 4 hours |
| High | 8 hours |
| Medium | 24 hours |
| Low | 48 hours |

**Note:** These SLA targets are project assumptions for analytical demonstration and do not represent official HCL SLA policies.

### Calculation Formulas

Resolution Time:

Resolution Time = Resolved Timestamp − Created Timestamp

First Response Time:

First Response Time = First Response Timestamp − Created Timestamp

SLA Deadline:

SLA Deadline = Created Timestamp + Priority-Based SLA Target

### SLA Classification

- **Within SLA:** Ticket resolved within the target.
- **Breached:** Resolution exceeded the target.
- **Pending:** Unresolved ticket still within the SLA deadline.
- **Overdue:** Unresolved ticket whose SLA deadline has passed.

The calculations use elapsed calendar hours, including weekends.

## 8. SQL Database Design

The project uses Oracle SQL for relational database management and analytical queries.

The Oracle database contains four main relational tables:

1. DEPARTMENTS
2. AGENTS
3. AGENT_DEPARTMENTS
4. TICKETS

### SQL Implementation

- Database schema creation.
- Master data insertion.
- Ticket data insertion.
- SLA-related queries.
- Analytical views.
- KPI queries.
- Database indexes.

The SQL scripts were executed and verified using Oracle Live SQL.

The database implementation supports ticket analysis, SLA reporting, and agent and department performance monitoring.

The Streamlit dashboard currently uses CSV-based data processing rather than a live Oracle database connection.

## 9. Advanced Analytics

The project includes multiple analytical modules.

### 9.1 Agent Performance

- Tickets resolved by each agent.
- Average resolution time.
- SLA breaches.
- Reopened tickets.

### 9.2 Department Analytics

- Department-wise ticket distribution.
- Workload analysis.
- SLA performance.

### 9.3 Ticket Aging

- Identification of pending tickets.
- Calculation of ticket age.
- Backlog classification.

### 9.4 Business Insights

- Priority distribution.
- Category distribution.
- Reopened ticket analysis.
- Escalation analysis.

## 10. CSV Upload and Automated Data Validation

The Streamlit dashboard supports uploading help-desk CSV files.

The validation module checks:

- Required columns.
- Missing required values.
- Duplicate ticket IDs.
- Invalid date values.
- Invalid priority values.
- Invalid reopened and escalation flags.

Invalid records are reported separately, while valid records continue through the analytics workflow.

The uploaded dataset is processed using the existing SLA calculation and dashboard analytics modules.

The functionality was verified using a CSV file containing 25 valid tickets.

## 11. Key Business Results

### 11.1 Overall Performance

| Metric | Result |
|---|---:|
| Total Tickets | 25 |
| Resolved Tickets | 21 |
| Open Tickets | 4 |
| Within SLA | 5 |
| Total SLA Breached | 20 |
| Pending SLA | 0 |
| Overall SLA Breach | 80.00% |
| Average Resolution Time | 30.48 hours |
| Reopened Tickets | 4 |
| Escalated Tickets | 7 |

### 11.2 Priority-wise Distribution

| Priority | Tickets |
|---|---:|
| Critical | 7 |
| High | 7 |
| Medium | 6 |
| Low | 5 |

### 11.3 Category-wise Distribution

| Category | Tickets |
|---|---:|
| Hardware | 5 |
| Network | 5 |
| Software | 5 |
| Access | 4 |
| Server | 4 |
| Security | 2 |

### 11.4 Additional SLA Insight

Out of 21 resolved tickets:

- 5 were resolved within SLA.
- 16 breached their SLA.
- Resolved-ticket SLA breach percentage was 76.19%.

The overall SLA breach percentage is 80%, because it also includes four overdue unresolved tickets.

All figures represent the project's sample dataset, not actual organizational performance.

## 12. Interactive Dashboards

### 12.1 Streamlit Dashboard

The interactive Streamlit dashboard provides:

- Executive Dashboard.
- SLA Performance.
- Department Analytics.
- Agent Performance Analysis.
- Ticket Aging Analysis.
- Business Insights.
- CSV upload functionality.
- Automated ticket validation.
- CSV export functionality.

The dashboard displays important KPIs, charts, and operational insights.

**Live Dashboard:**  
https://itsm-analytics-dashboard.streamlit.app/

### 12.2 Power BI Dashboard

The Power BI report includes:

- Total ticket KPI cards.
- Resolved and open ticket metrics.
- SLA breach analysis.
- Average resolution time.
- Priority-wise ticket analysis.
- Category-wise ticket analysis.
- Reopened and escalated ticket metrics.

The completed Power BI report is saved at:

`powerbi/ITSM_Analytics_Dashboard_Final.pbix`

## 13. Automated Testing

Pytest was used to validate SLA calculation functionality.

The automated test cases cover:

1. Tickets resolved within SLA.
2. Tickets breaching SLA.
3. Open tickets within SLA.
4. Overdue open tickets.
5. Exact SLA deadline conditions.
6. Critical priority SLA target.
7. High priority SLA target.
8. Medium priority SLA target.
9. Low priority SLA target.
10. Resolution time calculation.
11. First response time calculation.
12. SLA deadline calculation.
13. Weekend hours in resolution time.
14. Weekend handling in SLA deadlines.

**Testing Result: 14 tests passed successfully.**

## 14. Manual Verification

An independent Python datetime-based verification process was performed on all 25 tickets.

The calculated results were compared with the project's SLA calculation output.

All 25 ticket records passed the independent calculation-based verification checks.

This represents independent calculation-based verification, not a human audit.

## 15. Database Performance Considerations

Database indexes were created on selected ticket columns, including:

- Creation date.
- Resolution date.
- Department.
- Agent.
- Reopening timestamp.

These indexes are intended to support frequently used filtering and analytical queries.

No measured query performance improvement is claimed.

## 16. Limitations

1. The project currentsly uses a relatively small sample dataset of 25 tickets.
2. The SLA model uses calendar hours rather than business hours.
3. Four tickets remain unresolved and are overdue according to the analysis date.
4. Reopened ticket timestamps are missing for the four reopened records.
5. Actual second-cycle resolution time cannot be calculated without reopening timestamps.
6. The star schema is documented as a proposed analytical model, while the implemented Oracle database uses normalized relational tables.
7. The Streamlit dashboard uses CSV-based processing rather than a live Oracle database connection.
8. The project is not connected to HCL's internal ticketing system or APIs.
9. Production authentication and role-based access control are not implemented.
10. The dashboard is an analytical prototype and not a fully integrated enterprise ITSM production platform.

## 17. Future Scope

Potential future improvements include:

- Integration with authorized live ITSM ticketing APIs.
- Larger real-world datasets.
- Business-hours-based SLA calculations.
- Automated ticket assignment.
- Predictive SLA breach alerts.
- Machine learning-based ticket classification.
- Root-cause analysis.
- Real-time monitoring.
- Complete reopened-ticket lifecycle tracking.
- Role-based access and authentication.
- Enterprise-level deployment.

## 18. Conclusion

ITSM Analytics demonstrates how Python, Oracle SQL, Streamlit, and Power BI can be combined to analyze IT help-desk operations.

The project provides measurable insights into ticket resolution, SLA compliance, ticket aging, agent performance, department workload, and ticket categories.

The implementation includes data cleaning, automated CSV validation, analytical processing, SQL database management, automated testing, independent verification, and interactive dashboards.

The project demonstrates a practical foundation for data-driven IT service management and continuous service improvement.

---

**Project:** ITSM Analytics – Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

**Project Reference:** HCL Career – Project Serial No. 27