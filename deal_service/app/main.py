from fastapi import FastAPI
from .database import engine, Base
from .routers import deals, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(deals.router)
app.include_router(analytics.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}