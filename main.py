from fastapi import FastAPI, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from utils import load_data
import pandas as pd

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_report(db: Session):
    load_data(db)
    ## Simulate report generation logic
    print("Report generated")

@app.post("/trigger_report")
def trigger_report(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    report_id = "report_12345"  ##  Randomly generated report ID
    background_tasks.add_task(generate_report, db)
    return {"report_id": report_id}

@app.get("/get_report")
def get_report(report_id: str):
    report_data = pd.DataFrame({
        'store_id': ['store1', 'store2'],
        'uptime_last_hour': [60, 50],
        'uptime_last_day': [24, 22],
        'uptime_last_week': [168, 154],
        'downtime_last_hour': [0, 10],
        'downtime_last_day': [0, 2],
        'downtime_last_week': [0, 14]
    })

    ##  Save the report to a file
    report_file_path = f"reports/{report_id}.csv"
    report_data.to_csv(report_file_path, index=False)

    ##  Return the file path in the response
    return {"status": "Complete", "report_file": report_file_path}
