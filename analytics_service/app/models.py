from sqlalchemy import Column, Integer, Float, DateTime
from .database import Base

class AggregatedData(Base):
    __tablename__ = "analytics_cache"
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    total_deals = Column(Integer)
    total_revenue = Column(Float)
    avg_deal_size = Column(Float)
    customer_count = Column(Integer)