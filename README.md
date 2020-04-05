# Protype CBR

This prototype was built for a [search project I participate in](https://medium.com/@fndomariano/what-i-learned-in-a-search-project-8f1bf827ceb1) and also was my final paper. Its objective got to evaluate the quality of the water.

## Install

a) Configure environment file

```bash
$ cp .env.default .env
```

b) Up the docker containers

```bash
$ docker-compose up -d
```

c) Run migrations
```bash
$ docker-compose exec web python manage.py migrate --noinput
```

4) Access ```http://localhost:8080``` 
