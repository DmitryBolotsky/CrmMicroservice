from fastapi import APIRouter, Depends
from ..schemas import DateRange, SalesReport
from ..services import DataConnector, ReportGenerator

router = APIRouter(prefix="/sales", tags=["Analytics"])

@router.get("/report", response_model=SalesReport)
async def get_sales_report(date_range: DateRange = Depends()):
    deals = DataConnector.get_deals(date_range)
    return ReportGenerator.generate_sales_report(deals)