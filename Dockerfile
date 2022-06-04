FROM python:3.9-slim

WORKDIR /app

ADD . /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "src/main/app.py"]
