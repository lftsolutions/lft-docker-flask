# lft-docker-flask
A templated docker flask application service to be used as a starting point for future applications

## How to use
### Initial Setup
- `pipenv install` Needed to setup `Pipfile.lock`

### Docker
#### Build and Run
- `DOCKER_BUILDKIT=0 docker build -t lft-docker-flask --no-cache .`
- `docker run -p 8000:5000 lft-docker-flask`
- Once the app is up and running, go to `localhost:8000`

#### Cleanup
- `docker rm -f $(docker ps -aq)`
- `docker system`
