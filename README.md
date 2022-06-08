# flasklate
A dockerized flask template (`flasklate`) to be used as a bootstrap starting point for future projects.


## Getting Started
### Run as soon as you clone the repo
- `pipenv install` (Needed to setup `Pipfile.lock`)

### As you add new dependencies
- `pipenv install {dependency}` (Needed to keep `Pipfile` and `Pipfile.lock` in sync)


## Development
### Docker
#### Build and Run
- `DOCKER_BUILDKIT=0 docker build -t flasklate --no-cache .`
- `docker run -p 8000:5000 flasklate`
- Once the app is up and running, go to `localhost:8000`

#### System Cleanup
- `docker rm -f $(docker ps -aq)`
- `docker system prune`


## Testing
### Execute pytest
- `pipenv run pytest -v`

### Execute pytest-cov
- `pipenv run pytest --cov flasklate --cov-report html`