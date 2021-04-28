FROM python:3.9.4-alpine3.13

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /to-do-app

COPY . .

RUN apk update
RUN apk add build-base
RUN apk add musl-dev mariadb-dev gcc
RUN pip install -r requirements.txt

CMD ["python","manage.py", "runserver","-h","0.0.0.0"]
