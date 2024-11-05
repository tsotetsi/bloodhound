# bloodhound

## Getting Up and Running Locally With Docker

## Prerequisites

 - Docker - follow the installation [instructions](https://docs.docker.com/get-started/get-docker/#supported-platforms)  if you do not have it.
 - Docker Compose - refer to the [official documentation](https://docs.docker.com/compose/install/) for the installation guide.
 - Pre-commit - refer to the [official documentation](https://pre-commit.com/#install) for the pre-commit.

## Build the Stack
The build command can take a while, especially the first time you run this particular command on your machine.

```
$ docker compose -f docker-compose.local.yml build
```

If you want to emulate production env you can use `docker-compose.production.yml` instead.

Before doing any git commit, [pre-commit](https://pre-commit.com/#install) should be installed globally on your local machine, and then:

```
$ git init
$ pre-commit install
```

Failing to do so will result with a bunch of CI and Linter errors that can be avoided with pre-commit.
## Run the Stack

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development:

```
$ docker compose -f docker-compose.local.yml up
```

You can also set the environment variable COMPOSE_FILE pointing to docker-compose.local.yml like this:

```
$ export COMPOSE_FILE=docker-compose.local.yml
```

And then run:

```
$ docker compose up
```

To check the logs, you can run:

```
$ docker-compose logs
```

## Useful commands

 - `pip list --not-required --format=freeze > requirements/base.txt` Add only required deps to the base file.

## Database commands.
To get the postgres image-id, use the following command:

- `docker ps | grep postgres | awk '{print $1}'`
   then you would get something like: `cd2057ecd4d5` which is the postgres image.

- `docker exec -it <image-id> psql -U dev -d postgres -c "DROP DATABASE bloodhound;"` # Delete DB.(Fix me!)
- `docker exec -it <image-id> psql -U dev -d postgres -c "CREATE DATABASE bloodhound;` # Create DB.(Fix me!)

### Test coverage.

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest.

    $ pytest

### Run django commands agaqinst the image.
- `docker-compose run --rm django python manage.py createsuperuser`
