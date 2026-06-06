import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pathlib import Path

DATA_FILE = Path("defect_data.csv")

st.set_page_config(
    page_title="Manufacturing Defect Tracker",
    page_icon="🛠️",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df["date"] = pd.to_datetime(df["date"])
    return df

def save_record(record):
    df = pd.read_csv(DATA_FILE)
    new_row = pd.DataFrame([record])
    updated_df = pd.concat([df, new_row], ignore_index=True)
    updated_df.to_csv(DATA_FILE, index=False)

df = load_data()

st.title("Manufacturing Defect Tracker")
st.write(
    "Python analytics dashboard for tracking manufacturing defects, severity trends, "
    "process issues, root causes, and quality metrics."
)

st.sidebar.header("Filters")

process_filter = st.sidebar.multiselect(
    "Process",
    options=sorted(df["process"].unique()),
    default=sorted(df["process"].unique())
)

severity_filter = st.sidebar.multiselect(
    "Severity",
    options=sorted(df["severity"].unique()),
    default=sorted(df["severity"].unique())
)

status_filter = st.sidebar.multiselect(
    "Status",
    options=sorted(df["status"].unique()),
    default=sorted(df["status"].unique())
)

filtered_df = df[
    (df["process"].isin(process_filter)) &
    (df["severity"].isin(severity_filter)) &
    (df["status"].isin(status_filter))
]

total_defects = int(filtered_df["quantity_detected"].sum())
open_issues = int((filtered_df["status"] == "Open").sum())
high_severity = int((filtered_df["severity"] == "High").sum())
unique_parts = filtered_df["part_number"].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Defects", total_defects)
col2.metric("Open Issues", open_issues)
col3.metric("High Severity Records", high_severity)
col4.metric("Affected Part Numbers", unique_parts)

st.subheader("Defect Records")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("Manufacturing Quality Analytics")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.write("Defects by Process")
    process_counts = filtered_df.groupby("process")["quantity_detected"].sum()
    fig, ax = plt.subplots()
    process_counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Process")
    ax.set_ylabel("Quantity Detected")
    ax.set_title("Defect Quantity by Manufacturing Process")
    st.pyplot(fig)

with chart_col2:
    st.write("Defects by Severity")
    severity_counts = filtered_df.groupby("severity")["quantity_detected"].sum()
    fig, ax = plt.subplots()
    severity_counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Severity")
    ax.set_ylabel("Quantity Detected")
    ax.set_title("Defect Quantity by Severity")
    st.pyplot(fig)

st.subheader("Root Cause Summary")
root_cause_summary = (
    filtered_df.groupby("root_cause")["quantity_detected"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
st.dataframe(root_cause_summary, use_container_width=True)

st.subheader("Log a New Defect Record")

with st.form("defect_form"):
    new_date = st.date_input("Date", value=date.today())
    part_number = st.text_input("Part Number", placeholder="Example: F16-SKIN-500")
    process = st.selectbox("Process", ["Lamination", "Machining", "Coating", "Fabrication"])
    defect_type = st.text_input("Defect Type", placeholder="Example: Delamination")
    severity = st.selectbox("Severity", ["Low", "Medium", "High"])
    quantity_detected = st.number_input("Quantity Detected", min_value=1, step=1)
    root_cause = st.text_input("Root Cause", placeholder="Example: Tool wear")
    status = st.selectbox("Status", ["Open", "In Review", "Closed"])

    submitted = st.form_submit_button("Add Defect Record")

    if submitted:
        if not part_number or not defect_type or not root_cause:
            st.error("Please complete all required text fields.")
        else:
            record = {
                "date": new_date,
                "part_number": part_number,
                "process": process,
                "defect_type": defect_type,
                "severity": severity,
                "quantity_detected": quantity_detected,
                "root_cause": root_cause,
                "status": status
            }

            save_record(record)
            st.success("Defect record added successfully. Refresh the page to view updated data.")
