# flasklate
A templated docker flask application service to be used as a starting point for future applications

## How to use
### Initial Setup (Must run after cloning repo)
- `pipenv install` (Needed to setup `Pipfile.lock`)

### Docker
#### Build and Run
- `DOCKER_BUILDKIT=0 docker build -t flasklate --no-cache .`
- `docker run -p 8000:5000 flasklate`
- Once the app is up and running, go to `localhost:8000`

#### Cleanup
- `docker rm -f $(docker ps -aq)`
- `docker system prune`
