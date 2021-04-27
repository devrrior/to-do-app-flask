FROM python:3.9.4-alpine3.13

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /to-do-app

COPY . .

RUN apk add build-base
RUN pip install -r requirements.txt

CMD ["python","run.py"]
