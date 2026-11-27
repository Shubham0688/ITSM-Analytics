import pandas as pd
import streamlit as st
import plotly.express as px
from src.sla_calculator import calculate_sla


st.set_page_config(
    page_title="ITSM Analytics",
    page_icon="📊",
    layout="wide"
)


@st.cache_data(ttl=60)
def load_data():
    df = pd.read_csv("data/cleaned_tickets.csv")
    df = calculate_sla(df)
    return df


st.title("ITSM Analytics Dashboard")
st.write("Intelligent Help-Desk Ticket Analysis & SLA Monitoring System")

df = load_data()

st.sidebar.header("Dashboard Filters")

priorities = st.sidebar.multiselect(
    "Select Priority",
    options=sorted(df["priority"].dropna().unique()),
    default=sorted(df["priority"].dropna().unique())
)

departments = st.sidebar.multiselect(
    "Select Department",
    options=sorted(df["department"].dropna().unique()),
    default=sorted(df["department"].dropna().unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].dropna().unique()),
    default=sorted(df["category"].dropna().unique())
)

filtered_df = df[
    df["priority"].isin(priorities)
    & df["department"].isin(departments)
    & df["category"].isin(categories)
].copy()

total_tickets = len(filtered_df)

resolved_df = filtered_df[
    filtered_df["resolved_at"].notna()
]

breached_tickets = (
    filtered_df["sla_status"] == "Breached"
).sum()

within_sla = (
    filtered_df["sla_status"] == "Within SLA"
).sum()

sla_pending = (
    filtered_df["sla_status"] == "Pending"
).sum()

open_tickets = (
    filtered_df["resolved_at"].isna()
).sum()

avg_resolution = (
    resolved_df["resolution_time_hours"].mean()
    if not resolved_df.empty
    else 0
)

breach_percentage = (
    breached_tickets / total_tickets * 100
    if total_tickets > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tickets", total_tickets)
col2.metric("SLA Breach %", f"{breach_percentage:.2f}%")
col3.metric("Avg Resolution Time", f"{avg_resolution:.2f} hrs")
col4.metric("Open Tickets", open_tickets)

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.subheader("Tickets by Priority")

    priority_data = (
        filtered_df["priority"]
        .value_counts()
        .reindex(
            ["Critical", "High", "Medium", "Low"],
            fill_value=0
        )
        .reset_index()
    )

    priority_data.columns = ["Priority", "Tickets"]

    fig = px.bar(
        priority_data,
        x="Priority",
        y="Tickets",
        title="Priority-wise Ticket Distribution",
        text="Tickets"
    )

    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("Tickets by Category")

    category_data = (
        filtered_df["category"]
        .value_counts()
        .reset_index()
    )

    category_data.columns = ["Category", "Tickets"]

    fig = px.pie(
        category_data,
        names="Category",
        values="Tickets",
        title="Category-wise Ticket Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

col7, col8 = st.columns(2)

with col7:
    st.subheader("SLA Performance")

    sla_data = pd.DataFrame({
        "SLA Status": [
            "Within SLA",
            "Breached",
            "Pending"
        ],
        "Tickets": [
            within_sla,
            breached_tickets,
            sla_pending
        ]
    })

    fig = px.bar(
        sla_data,
        x="SLA Status",
        y="Tickets",
        color="SLA Status",
        text="Tickets",
        title="SLA Status Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col8:
    st.subheader("Department-wise Tickets")

    department_data = (
        filtered_df["department"]
        .value_counts()
        .reset_index()
    )

    department_data.columns = ["Department", "Tickets"]

    fig = px.bar(
        department_data,
        x="Department",
        y="Tickets",
        text="Tickets",
        title="Department-wise Ticket Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Ticket Details")

st.dataframe(
    filtered_df[
        [
            "ticket_id",
            "priority",
            "category",
            "department",
            "agent_id",
            "status",
            "resolution_time_hours",
            "sla_target_hours",
            "sla_deadline",
            "sla_status",
            "sla_breached",
            "reopened",
            "escalated"
        ]
    ],
    use_container_width=True
)

st.subheader("Business Insights")

if not filtered_df.empty:
    st.write(f"Total tickets analyzed: {total_tickets}")
    st.write(f"Tickets resolved: {len(resolved_df)}")
    st.write(f"Tickets within SLA: {within_sla}")
    st.write(f"Tickets breaching SLA: {breached_tickets}")
    st.write(f"Tickets with pending SLA: {sla_pending}")
    st.write(f"Tickets currently open: {open_tickets}")
    st.write(
        f"Reopened tickets: "
        f"{(filtered_df['reopened'] == 'Yes').sum()}"
    )
    st.write(
        f"Escalated tickets: "
        f"{(filtered_df['escalated'] == 'Yes').sum()}"
    )
else:
    st.info("No tickets match the selected filters.")

st.divider()

st.title("Advanced Analytics")

st.subheader("Agent Performance Analysis")

resolved_tickets = filtered_df[
    filtered_df["resolved_at"].notna()
].copy()

agent_report = resolved_tickets.groupby("agent_id").agg(
    tickets_resolved=("ticket_id", "count"),
    avg_resolution_hours=("resolution_time_hours", "mean"),
    sla_breaches=("sla_status", lambda x: (x == "Breached").sum()),
    reopened_tickets=("reopened", lambda x: (x == "Yes").sum())
).reset_index()

agent_report["avg_resolution_hours"] = (
    agent_report["avg_resolution_hours"].round(2)
)

if not agent_report.empty:
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            agent_report,
            x="agent_id",
            y="tickets_resolved",
            title="Tickets Resolved by Agent",
            text="tickets_resolved"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(
            agent_report,
            x="agent_id",
            y="avg_resolution_hours",
            title="Average Resolution Time by Agent",
            text="avg_resolution_hours"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(agent_report, use_container_width=True)

else:
    st.info("No resolved tickets available for agent analysis.")

st.divider()

st.subheader("Ticket Aging Analysis")

pending_tickets = filtered_df[
    filtered_df["resolved_at"].isna()
].copy()

if not pending_tickets.empty:
    pending_tickets["pending_hours"] = (
        pd.Timestamp.now() - pending_tickets["created_at"]
    ).dt.total_seconds() / 3600

    pending_tickets["aging_category"] = pd.cut(
        pending_tickets["pending_hours"],
        bins=[0, 24, 48, 168, float("inf")],
        labels=[
            "Under 24 Hours",
            "24-48 Hours",
            "2-7 Days",
            "Above 7 Days"
        ],
        include_lowest=True
    )

    aging_data = (
        pending_tickets["aging_category"]
        .value_counts()
        .reindex(
            [
                "Under 24 Hours",
                "24-48 Hours",
                "2-7 Days",
                "Above 7 Days"
            ],
            fill_value=0
        )
        .reset_index()
    )

    aging_data.columns = ["Aging Category", "Tickets"]

    fig = px.bar(
        aging_data,
        x="Aging Category",
        y="Tickets",
        text="Tickets",
        title="Pending Tickets by Aging Category"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        pending_tickets[
            [
                "ticket_id",
                "priority",
                "department",
                "agent_id",
                "pending_hours",
                "aging_category",
                "sla_status"
            ]
        ],
        use_container_width=True
    )

else:
    st.success("No pending tickets available.")

st.divider()

st.subheader("Export Ticket Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="itsm_ticket_report.csv",
    mime="text/csv"
)