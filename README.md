# Python Manufacturing Defect Tracker

A Python analytics dashboard for tracking manufacturing defects, severity trends, process issues, root causes, and quality metrics. This project connects manufacturing engineering experience with software development by using Python to organize production defect data and generate quality insights.

## Tech Stack

* Python
* Streamlit
* pandas
* matplotlib
* CSV data storage
* Data filtering
* Quality analytics
* Git/GitHub

## Features

* Load manufacturing defect records from a CSV dataset
* Filter defects by manufacturing process, severity, and status
* Track total defect quantity, open issues, high-severity records, and affected part numbers
* Visualize defect quantity by process
* Visualize defect quantity by severity
* Generate root-cause summaries for process improvement
* Add new defect records through an interactive form
* Store new records back into the CSV dataset

## Project Structure

```text
python-manufacturing-defect-tracker/
├── app.py
├── defect_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Fields

```text
date                  Date the defect was recorded
part_number           Affected part or component number
process               Manufacturing process where the issue occurred
defect_type           Type of defect found
severity              Low, Medium, or High severity
quantity_detected     Number of defects detected
root_cause            Suspected or confirmed cause of the issue
status                Open, In Review, or Closed
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

## What I Built

I developed the Streamlit dashboard, CSV-based data workflow, filtering logic, manufacturing quality metrics, visual analytics, root-cause summary table, and defect entry form. The project was designed to demonstrate how Python can be used for production quality tracking, process analysis, and technical reporting.

## Future Improvements

* Add database storage using SQLite or PostgreSQL
* Add user authentication
* Add exportable PDF or Excel reports
* Add trend analysis by week or month
* Add predictive defect-risk scoring
* Deploy the dashboard online
