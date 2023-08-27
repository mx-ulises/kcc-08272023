FROM python:alpine3.18 AS base

COPY main.py .
ENTRYPOINT ["python3", "main.py"]
