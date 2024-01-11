FROM python:3.11.7-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003

ENV "TIER_KEY" "your_tier_key"
CMD ["python3", "/app/src/main.py"]
