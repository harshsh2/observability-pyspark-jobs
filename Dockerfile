FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements_kafka.txt .
RUN pip install --no-cache-dir -r requirements_kafka.txt

# Copy application code
COPY . .

# Ensure logs flush immediately
ENV PYTHONUNBUFFERED=1

# Default command (can be overridden by K8s)
CMD ["python", "kafka_consumer.py"]
