# Restaurant Monitoring System

This project is a backend application built using FastAPI that monitors the online status of restaurants in the US. The system ingests data from CSV files and generates uptime/downtime reports based on periodic polls, business hours, and time zones. It also includes endpoints to trigger report generation and fetch the report status or CSV output.

## Features

- Ingests store status, business hours, and time zone data from CSV files.
- Calculates uptime/downtime metrics for the last hour, day, and week.
- Asynchronous report generation using FastAPI's `BackgroundTasks`.
- RESTful APIs for triggering report generation and retrieving report data.

## Project Structure

```plaintext
restaurant_monitoring/
├── data/
│   ├── store_data.csv
│   ├── business_hours.csv
│   └── timezones.csv
├── main.py
├── models.py
├── database.py
├── utils.py
├── requirements.txt
└── README.md

## Project Execution

1. Run the FastAPI Application:
         uvicorn main:app --reload

2. Trigger Report Generation:
         curl -X POST "http://127.0.0.1:8000/trigger_report"

3. Fetch Report Status and Results:
         curl -X GET "http://127.0.0.1:8000/get_report?report_id=<your_report_id>"

4. Check Uptime and Downtime for a Specific Store:
        curl -X GET "http://127.0.0.1:8000/get_store_uptime?store_id=<store_id>"

Example Output:

The output from the /get_report endpoint might look like this:

    {
    "status": "Complete",
    "csv": "store_id,uptime_last_hour,uptime_last_day,uptime_last_week,downtime_last_hour,downtime_last_day,downtime_last_week\r\nstore1,60,24,168,0,0,0\r\nstore2,50,22,154,10,2,14\r\n"
    }

Reports Folder:
  It has Executed Output csv file 

         