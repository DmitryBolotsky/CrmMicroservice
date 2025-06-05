# Этап сборки
FROM python:3.9-alpine as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Финальный этап
FROM python:3.9-alpine
WORKDIR /app
RUN adduser -D rootless
USER rootless
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]