FROM python:3.11-slim

WORKDIR /build

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /app
