from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DealBase(BaseModel):
    customer_id: int
    amount: float
    stage: str = "proposal"

class DealCreate(DealBase):
    pass

class DealResponse(DealBase):
    id: int
    created_at: datetime
    customer_name: Optional[str] = None  # Будет заполняться через relationship

    class Config:
        from_attributes = True

class DealAnalytics(BaseModel):
    total_deals: int
    total_amount: float
    avg_deal_size: float
    win_rate: float