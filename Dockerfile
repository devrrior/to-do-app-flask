FROM python:3.9.4-alpine3.13

WORKDIR /todo-app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && apk update \
    && apk add build-base \
    && apk add musl-dev mariadb-dev gcc \
    && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python","run.py"]
