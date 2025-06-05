from fastapi import FastAPI
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Deal Service",
    description="Управление сделками и продажами"
)

from .routers import deals, analytics
app.include_router(deals.router)
app.include_router(analytics.router)