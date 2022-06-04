FROM python:3.9-slim

WORKDIR /app

ADD . /app

RUN pip install pipenv

RUN pipenv install --system --deploy

RUN ls -la
RUN ls app/

RUN pwd

CMD ["python", "run.py"]
