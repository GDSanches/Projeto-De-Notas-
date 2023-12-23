# Deploy Django using Nginx, Celery, Redis and Postgresql with Docker

Where it is described how this boilerplate was created from scratch so that you can build your own.

## Advantages
1. Ready to use with your django project.
2. Combined with NGINX, Redis, Celery to handle relevent things.
3. Alpine based images are used, so that sizes of the images are compartively low.
4. Now comes built it with Numpy, Scipy and Pandas support. So you can integrate your datascience projects with this. [Instructions](#now-featuring-numpy-scipy-and-pandas) for integrating these libraries are also shared in the `Dockerfile`.
5. With Numpy, Pandas and Scipy dependecies installed, the total size is 657MB(may differ if you have more packages). Without these, size reduces to 390MB.
6. Now comes with support to install [Pillow](https://pypi.org/project/Pillow/) using django.

## Now Featuring Numpy, Scipy and Pandas
In the [**`Dockerfile`**](https://gitlab.com/braga1233/docker-django-base-ifg-web/blob/master/compose/django/Dockerfile), there are detailed instructions on how to install data science dependencies.

**PS:** Here is a [**__`gist`__**](https://gitlab.com/braga1233/docker-django-base-ifg-web/870d7a51238ddfa4b50375086c12a4f5) which is more useful for Numpy, Pandas, Scipy etc. And it is usable with this project's [`docker-compose.yml`](https://gitlab.com/braga1233/docker-django-base-ifg-web/blob/master/docker-compose.yml) file. Just you need to replace the `Dockerfile` from [*./compose*](https://gitlab.com/braga1233/docker-django-base-ifg-web/blob/master/compose) directory with the one in the *gist*.


## Basic Usage
1. First run **`make build`** inside root directory.
2. Then run **`make up`** to start up the project for first time.
3. Use/update environment variables from [**`.envs`**](https://gitlab.com/braga1233/docker-django-base-ifg-web/blob/master/.envs) folder.

Checkout the [commands](#commands) section for more usage.

## Preview
A default Django project resides in `src` directory. So, when you start the project, you will see the following screen in `8000` port:


## Commands
To use this project, run this commands:

1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.

## License
[MIT](https://github.com/ruddra/docker-django/blob/master/LICENSE).

## Contribute

Feel free to fork and create PR.