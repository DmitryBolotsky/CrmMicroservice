from pydantic import BaseModel
from datetime import date

class DateRange(BaseModel):
    start_date: date
    end_date: date

class SalesReport(BaseModel):
    period: str
    total_revenue: float
    deals_closed: int
    conversion_rate: float
    top_customers: list[dict]

class CustomerReport(BaseModel):
    total_customers: int
    new_customers: int
    churn_rate: float