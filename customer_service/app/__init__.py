from fastapi import FastAPI
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer Service",
    description="Управление клиентской базой"
)

from .routers import customers
app.include_router(customers.router)