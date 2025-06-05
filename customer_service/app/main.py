from fastapi import FastAPI, Depends
from .routers import customers
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(customers.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}