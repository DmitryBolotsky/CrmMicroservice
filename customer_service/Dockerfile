# Этап сборки
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Финальный образ
FROM python:3.9-slim
WORKDIR /app

# Копируем только необходимое
COPY --from=builder /root/.local /root/.local
COPY ./customer_service ./customer_service

# Настройки безопасности
RUN useradd -m serviceuser && chown -R serviceuser /app
USER serviceuser

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["uvicorn", "customer_service.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]