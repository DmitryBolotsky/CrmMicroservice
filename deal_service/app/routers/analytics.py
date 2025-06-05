from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/deals", response_model=schemas.DealAnalytics)
def get_deals_analytics(
    db: Session = Depends(database.get_db),
    current_user: str = Depends(dependencies.get_current_user)
):
    total = db.query(func.count(models.Deal.id)).scalar()
    total_amount = db.query(func.sum(models.Deal.amount)).scalar() or 0
    won = db.query(func.count(models.Deal.id)).filter(models.Deal.stage == "closed").scalar()
    
    return {
        "total_deals": total,
        "total_amount": total_amount,
        "avg_deal_size": total_amount / total if total else 0,
        "win_rate": won / total if total else 0
    }