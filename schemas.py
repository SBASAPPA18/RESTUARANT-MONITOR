from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StoreDataCreate(BaseModel):
    store_id: str
    timestamp_utc: datetime
    status: str

class BusinessHoursCreate(BaseModel):
    store_id: str
    dayOfWeek: int
    start_time_local: str
    end_time_local: str

class TimezoneCreate(BaseModel):
    store_id: str
    timezone_str: Optional[str] = "America/Chicago"
