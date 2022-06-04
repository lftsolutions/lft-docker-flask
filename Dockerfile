FROM python:3.9-slim

# Setup
WORKDIR /app
ADD . /app

# Configure
RUN pip install pipenv
RUN pipenv install --system --deploy

# Run
CMD ["python", "flasklate.py"]
