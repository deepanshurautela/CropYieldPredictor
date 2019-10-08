FROM python:latest
COPY . /app/
WORKDIR /app/
RUN apt-get update
RUN pip install -r requirements.txt && \
    python start.py
EXPOSE 5000
