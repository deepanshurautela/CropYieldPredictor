FROM python:rc-alpine3.10
COPY . /app/
WORKDIR /app/
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install -r requirements.txt && \
    python start.py
EXPOSE 5000
