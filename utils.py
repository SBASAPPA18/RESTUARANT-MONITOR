import pandas as pd
from sqlalchemy.orm import Session
from models import StoreData, BusinessHours, Timezone
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def load_data(session: Session):
    try:
        # Load data from CSV files
        store_data = pd.read_csv('data/store_data.csv')
        business_hours = pd.read_csv('data/business_hours.csv')
        timezones = pd.read_csv('data/timezones.csv')

        logging.info("Loaded data from CSV files successfully.")

        # Add store data to the database
        for _, row in store_data.iterrows():
            store_entry = StoreData(
                store_id=row['store_id'],
                timestamp_utc=pd.to_datetime(row['timestamp_utc']),
                status=row['status']
            )
            session.add(store_entry)

        # Add business hours to the database
        for _, row in business_hours.iterrows():
            business_hours_entry = BusinessHours(
                store_id=row['store_id'],
                dayOfWeek=row['dayOfWeek'],
                start_time_local=pd.to_datetime(row['start_time_local']).time(),
                end_time_local=pd.to_datetime(row['end_time_local']).time()
            )
            session.add(business_hours_entry)

        # Add timezones to the database
        for _, row in timezones.iterrows():
            timezone_entry = Timezone(
                store_id=row['store_id'],
                timezone_str=row['timezone_str']
            )
            session.add(timezone_entry)

        # Commit the transaction
        session.commit()
        logging.info("Data committed to the database successfully.")

    except Exception as e:
        session.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise
