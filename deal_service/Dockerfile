FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user gunicorn==20.1.0 -r requirements.txt

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./app ./app

RUN useradd -m serviceuser && \
    chown -R serviceuser /app
USER serviceuser

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000", "--workers", "4"]