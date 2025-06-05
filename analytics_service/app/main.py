from fastapi import FastAPI
from .routers import sales, customers
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Analytics Service")
app.include_router(sales.router)
app.include_router(customers.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}