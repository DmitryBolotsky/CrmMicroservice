from fastapi import APIRouter
from datetime import datetime, timedelta
from ..schemas import CustomerReport
from ..services.data_connector import DataConnector

router = APIRouter(prefix="/customers", tags=["Customer Analytics"])

@router.get("/report", response_model=CustomerReport)
async def get_customer_report():
    # Получаем всех клиентов из Customer Service
    customers = DataConnector.get_customers()
    
    if not customers:
        return {
            "total_customers": 0,
            "new_customers_week": 0,
            "active_customers": 0
        }

    # Текущая дата для расчетов
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    # Базовые метрики
    new_customers_week = sum(
        1 for c in customers 
        if datetime.strptime(c["created_at"], "%Y-%m-%d") > week_ago
    )

    active_customers = sum(
        1 for c in customers 
        if datetime.strptime(c["last_activity"], "%Y-%m-%d") > month_ago
    )

    return {
        "total_customers": len(customers),
        "new_customers_week": new_customers_week,
        "active_customers": active_customers,
        "activity_percentage": round((active_customers / len(customers)) * 100, 1)
    }