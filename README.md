# ITSM Analytics
## Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

### 1. Project Overview

ITSM Analytics is a data-driven IT Service Management analytics solution designed to analyze help-desk tickets, monitor Service Level Agreement (SLA) compliance, evaluate support team performance, and generate actionable operational insights.

The system combines Python-based data processing, Oracle SQL analytics, Power BI reporting, and an interactive Streamlit dashboard.

It also supports CSV-based ticket ingestion with automated data validation, allowing users to analyze help-desk exports without manually modifying the source dataset.

### 2. Key Features

- Automated ticket data cleaning and preprocessing.
- CSV upload and ticket data ingestion.
- Automated validation of uploaded ticket records.
- Missing-value and duplicate-ticket detection.
- Invalid date and priority validation.
- Priority-based SLA calculation.
- SLA deadline and breach monitoring.
- Open-ticket and backlog monitoring.
- Ticket aging analysis.
- Agent performance analytics.
- Department-wise ticket analysis.
- Reopened and escalated ticket analysis.
- Interactive Streamlit dashboard.
- Interactive Plotly visualizations.
- Power BI analytical dashboard.
- Oracle SQL database schema, views, queries, and indexes.
- CSV report export.
- Automated testing using Pytest.
- Business insights and data quality reports.

### 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and business logic |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Interactive analytics dashboard |
| Oracle SQL | Relational database and analytical queries |
| Power BI | Business intelligence reporting |
| Pytest | Automated testing |
| Git & GitHub | Version control |

### 4. Project Architecture

The solution follows a modular analytics workflow:

1. Ticket data is loaded from CSV files.
2. Data cleaning and validation are performed.
3. SLA calculations are applied.
4. Python generates analytical outputs.
5. Oracle SQL supports relational data management and KPI queries.
6. Streamlit presents interactive analytics.
7. Power BI provides business intelligence reporting.
8. Users can export filtered ticket reports.

### 5. SLA Configuration

| Priority | SLA Target |
|---|---:|
| Critical | 4 Hours |
| High | 8 Hours |
| Medium | 24 Hours |
| Low | 48 Hours |

These SLA targets are project assumptions and are not official HCL or organizational SLA policies.

Resolution time is calculated using elapsed calendar hours, including weekends.

### 6. CSV Upload and Data Validation

The dashboard supports uploading help-desk CSV exports.

The validation module checks:

- Required columns.
- Missing required values.
- Duplicate ticket IDs.
- Invalid date values.
- Invalid priority values.
- Invalid reopened and escalation flags.

Records with validation issues are reported separately. Valid records can continue through the analytics workflow.

Expected CSV fields:

`ticket_id, created_at, first_response_at, resolved_at, closed_at, priority, category, department, agent_id, status, reopened, escalated`

### 7. Project Structure

```text
ITSM-Analytics/
│
├── data/
│   ├── raw_tickets.csv
│   ├── cleaned_tickets.csv
│   └── ITSM_Analytics_Dashboard_Final.pbix
│
├── src/
│   ├── data_cleaning.py
│   ├── data_quality.py
│   ├── sla_calculator.py
│   ├── ticket_validator.py
│   ├── advanced_analytics.py
│   ├── business_insights.py
│   └── generate_sql_seed.py
│
├── database/
│   ├── schema.sql
│   ├── queries.sql
│   ├── views.sql
│   ├── kpi_queries.sql
│   ├── indexes.sql
│   ├── insert_tickets.sql
│   └── insert_master_data.sql
│
├── dashboard/
│   └── app.py
│
├── powerbi/
│   └── ITSM_Analytics_Dashboard_Final.pbix
│
├── tests/
│   └── test_sla_calculator.py
│
├── reports/
│   ├── data_quality_report.csv
│   ├── manual_verification.csv
│   ├── ER_Diagram_Documentation.md
│   ├── Final_Project_Report.md
│   └── screenshots/
│
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md
```

### 8. Installation and Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 9. Running the Project

Data cleaning:

```bash
python src/data_cleaning.py
```

Data quality analysis:

```bash
python src/data_quality.py
```

SLA calculation:

```bash
python src/sla_calculator.py
```

Advanced analytics:

```bash
python src/advanced_analytics.py
```

Business insights:

```bash
python src/business_insights.py
```

Launch the Streamlit dashboard:

```bash
python -m streamlit run dashboard/app.py
```

Run automated tests:

```bash
python -m pytest tests/test_sla_calculator.py -v
```

### 10. Sample Dataset Results

The current sample dataset contains 25 tickets.

| Metric | Result |
|---|---:|
| Total Tickets | 25 |
| Resolved Tickets | 21 |
| Open Tickets | 4 |
| Within SLA | 5 |
| Total SLA Breached | 20 |
| Overall SLA Breach Percentage | 80.00% |
| Resolved Tickets Breached | 16 |
| Resolved-Only Breach Percentage | 76.19% |
| Reopened Tickets | 4 |
| Escalated Tickets | 7 |

The overall breach percentage includes overdue unresolved tickets. The resolved-only breach percentage considers only resolved tickets.

These figures represent the project's sample dataset and not actual organizational performance.


## 11. Project Validation and Limitations

- Oracle SQL schema, master data, ticket data, views, KPI queries, and indexes were executed and verified in Oracle Live SQL.
- Power BI dashboard has been developed and saved as `powerbi/ITSM_Analytics_Dashboard_Final.pbix`.
- 14 automated tests passed successfully.
- All 25 sample tickets passed the data quality validation.
- The project uses a sample dataset and is not connected to HCL's internal ticketing system.
- SLA targets are project assumptions and use calendar hours.
- Reopened ticket timestamps are not available, so second-cycle resolution time cannot be calculated.
- Production authentication and role-based access control are not implemented.

## 12. Future Scope

- Integration with authorized live ITSM APIs.
- Real-time ticket synchronization and monitoring.
- Role-based access control.
- Automated SLA notifications and alerts.
- Larger datasets and predictive analytics.
- Enterprise-level deployment.

## 13. Project Objective

The objective is to transform raw IT help-desk ticket data into meaningful operational insights that help organizations monitor SLA compliance, improve support team performance, and make data-driven decisions.

## 14. Author

Developed as a portfolio project demonstrating Python analytics, SQL, data visualization, SLA monitoring, and IT service management concepts.


### 15. Project Objective

The objective of ITSM Analytics is to transform raw help-desk ticket data into meaningful operational insights, helping support teams monitor SLA compliance, understand ticket backlogs, evaluate agent performance, and support data-driven IT service management decisions.

### 16. Author

