from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Deal(Base):
    __tablename__ = "deals"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    amount = Column(Float, nullable=False)
    stage = Column(String(50), default="proposal")  # proposal/negotiation/closed/lost
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Для связи с Customer Service (если используется единая БД)
    customer = relationship("Customer", lazy="joined")