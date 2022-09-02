FROM python:3.10

WORKDIR /docker-test

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

EXPOSE 8000

COPY ./pre-start.sh /docker-test/pre-start.sh

CMD chmod +x /docker-test/pre-start.sh