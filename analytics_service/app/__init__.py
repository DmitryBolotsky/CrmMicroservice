from fastapi import FastAPI

app = FastAPI(
    title="Analytics Service",
    description="Сервис аналитики и отчетов"
)

from .routers import sales, customers
app.include_router(sales.router)
app.include_router(customers.router)