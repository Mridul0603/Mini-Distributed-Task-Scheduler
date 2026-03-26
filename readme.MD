# Mini Distributed Task Scheduler

A simplified Airflow-like task orchestration system built using Flask, Celery, and .

## Architecture

Client → Flask API → Redis Queue → Celery Worker → Task Execution

## Features
- DAG submission and validation
- Asynchronous task execution
- Redis-based message broker
- Celery worker processing

## Tech Stack
- Python
- Flask
- Celery
- Redis
