from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(prefix="/deals", tags=["deals"])

@router.post("/", response_model=schemas.DealResponse)
def create_deal(
    deal: schemas.DealCreate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(dependencies.get_current_user)
):
    db_deal = models.Deal(**deal.model_dump())
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal

@router.get("/", response_model=List[schemas.DealResponse])
def read_deals(
    stage: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(dependencies.get_current_user)
):
    query = db.query(models.Deal)
    if stage:
        query = query.filter(models.Deal.stage == stage)
    return query.offset(skip).limit(limit).all()