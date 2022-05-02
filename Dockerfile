# syntax=docker/dockerfile:1
FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /lunch_place
COPY requirements.txt /lunch_place/
RUN pip install -r requirements.txt
COPY . /lunch_place/