FROM python:3.9-slim

# Setup
WORKDIR /app
ADD . /app

# Configure
RUN pip install pipenv
RUN pipenv install --system --deploy

# Run
CMD ["python", "lft_docker_flask.py"]
