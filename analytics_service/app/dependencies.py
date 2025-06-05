from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Optional
import requests

# Базовые зависимости (аналогичны другим сервисам)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Конфигурация (лучше вынести в .env)
SECRET_KEY = "your-analytics-secret"
ALGORITHM = "HS256"
SERVICES_CONFIG = {
    "customer_service": "http://customer-service:8001",
    "deal_service": "http://deal-service:8002"
}

async def verify_token(token: str = Depends(oauth2_scheme)):
    """Валидация JWT токена"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")  # Возвращаем email/user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

async def fetch_external_data(service: str, endpoint: str):
    """Общая зависимость для запросов к другим сервисам"""
    async def inner(token: str = Depends(oauth2_scheme)):
        url = f"{SERVICES_CONFIG[service]}/{endpoint}"
        headers = {"Authorization": f"Bearer {token}"}
        
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="External service request failed"
            )
        return response.json()
    return inner

# Специфичные зависимости для аналитики
get_customers_data = fetch_external_data("customer_service", "customers")
get_deals_data = fetch_external_data("deal_service", "deals")