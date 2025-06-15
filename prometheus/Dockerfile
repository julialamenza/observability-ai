FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir prometheus_client

CMD ["python", "log_exporter.py"]
