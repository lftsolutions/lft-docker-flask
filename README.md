#TODO clean up docker commands

# flasklate
A dockerized flask template (`flasklate`) to be used as a bootstrap starting point for future projects.

***
## ✨ Dev
[http://localhost:8000/](http://localhost:8000/)
```shell 
docker-compose down -v && \
    docker system prune -af && \
    docker-compose up --build
```
```shell
# debug
docker-compose logs -f
```
```shell
# login and verify database
docker-compose exec db psql --username=$POSTGRES_USER --dbname=$POSTGRES_PASSWORD
test_flask_dev=# \l

# create user table and login to verify
docker-compose exec web python manage.py seed_db
docker-compose exec db psql --username=$POSTGRES_USER --dbname=$POSTGRES_PASSWORD
test_flask_dev=# \dt
```
```shell
#cleanup
docker-compose down -v && \
    docker system prune -af
```