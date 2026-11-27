# ITSM Analytics – Intelligent Help-Desk Ticket Analysis & SLA Monitoring System

## 1. Project Overview

ITSM Analytics is a Python-based help-desk ticket analysis and SLA monitoring system. It helps analyze IT support tickets, monitor SLA performance, evaluate agent productivity, and generate business insights.

## 2. Key Features

- Automated ticket data cleaning.
- Duplicate and missing-value validation.
- Resolution time calculation.
- Priority-based SLA monitoring.
- SLA breach percentage calculation.
- Agent performance analysis.
- Department-wise ticket analysis.
- Ticket aging and backlog monitoring.
- Reopened and escalated ticket analysis.
- Interactive Streamlit dashboard.
- Interactive Plotly charts.
- CSV export functionality.
- Automated testing using Pytest.
- Business insights report generation.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive charts |
| Streamlit | Dashboard |
| Oracle SQL | Database scripts |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## 4. Project Structure

```text
ITSM-Analytics/
├── data/
├── notebooks/
├── src/
│   ├── data_cleaning.py
│   ├── sla_calculator.py
│   ├── data_quality.py
│   ├── advanced_analytics.py
│   └── business_insights.py
├── database/
│   ├── schema.sql
│   ├── queries.sql
│   ├── views.sql
│   └── kpi_queries.sql
├── dashboard/
│   └── app.py
├── tests/
│   └── test_sla_calculator.py
├── reports/
├── powerbi/
├── requirements.txt
└── README.md
```

## 5. SLA Configuration

| Priority | SLA Target |
|---|---:|
| Critical | 4 Hours |
| High | 8 Hours |
| Medium | 24 Hours |
| Low | 48 Hours |

These are example project assumptions, not official organizational SLA policies. Resolution time currently uses elapsed calendar hours.

## 6. Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Open the project folder:

```bash
cd ITSM-Analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 7. Running the Project

Data cleaning:

```bash
python src/data_cleaning.py
```

SLA calculation:

```bash
python src/sla_calculator.py
```

Data quality validation:

```bash
python src/data_quality.py
```

Advanced analytics:

```bash
python src/advanced_analytics.py
```

Business insights:

```bash
python src/business_insights.py
```

Launch dashboard:

```bash
python -m streamlit run dashboard/app.py
```

Run automated tests:

```bash
python -m pytest -v
```

## 8. Current Dataset Results

The current sample dataset contains 25 tickets.

| Metric | Result |
|---|---:|
| Total Tickets | 25 |
| Resolved Tickets | 21 |
| Open Tickets | 4 |
| Within SLA | 5 |
| SLA Breached | 16 |
| SLA Breach Percentage | 76.19% |
| Reopened Tickets | 4 |
| Escalated Tickets | 7 |

These results are based on the project's sample dataset, not real organizational statistics.

## 9. Data Quality

The validation module checks missing IDs, duplicate IDs, invalid priorities, date inconsistencies, missing departments and categories, and invalid reopened or escalation values.

The current dataset passed all implemented data-quality checks.

## 10. Automated Testing

The project includes five automated tests:

1. Ticket within SLA.
2. Ticket breaching SLA.
3. Open ticket.
4. Exact SLA deadline.
5. SLA target validation.

**Current result: 5 tests passed.**

## 11. Database

Oracle SQL scripts have been prepared for table creation, SLA queries, analytical views, and KPI calculations.

Oracle database execution and integration are not yet completed.

## 12. Future Scope

- Oracle database integration.
- Power BI dashboard development.
- More extensive automated testing.
- Real-time ticket monitoring.
- Advanced reporting and analytics.
- Wider deployment.

## 13. Project Objective

The objective is to transform raw IT help-desk ticket data into meaningful operational insights that help organizations monitor SLA compliance, improve support team performance, and make data-driven decisions.

## 14. Author

Developed as a portfolio project demonstrating Python analytics, SQL, data visualization, SLA monitoring, and IT service management concepts.