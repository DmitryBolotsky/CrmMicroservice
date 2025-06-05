from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
import models, schemas, utils
from database import SessionLocal, engine
from redis_cache import redis_client

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Проверка, что пользователь не существует
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Хеширование пароля и сохранение пользователя
    hashed_password = utils.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    
    # Генерация токена
    access_token = utils.create_access_token(data={"sub": user.email})
    redis_client.set(access_token, user.email, ex=1800)  # Сохраняем токен в Redis на 30 мин
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Проверка пользователя
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    # Генерация токена
    access_token = utils.create_access_token(data={"sub": user.email})
    redis_client.set(access_token, user.email, ex=1800)  # Кешируем токен
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
def read_current_user(token: str):
    email = redis_client.get(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"email": email.decode("utf-8")}