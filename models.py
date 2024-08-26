from sqlalchemy import Column, Integer, String, Time, DateTime
from database import Base

class StoreData(Base):
    __tablename__ = "store_data"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, index=True)
    timestamp_utc = Column(DateTime)
    status = Column(String)

class BusinessHours(Base):
    __tablename__ = "business_hours"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, index=True)
    dayOfWeek = Column(Integer)
    start_time_local = Column(Time)
    end_time_local = Column(Time)

class Timezone(Base):
    __tablename__ = "timezone"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, index=True)
    timezone_str = Column(String)
