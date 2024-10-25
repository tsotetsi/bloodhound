# Pull official base image.
FROM python:3.11.4-slim-buster AS python

# Python build stage.
FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=local

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt

# Python 'run' stage.
FROM python AS python-run-stage

ARG APP_HOME=/app

# Set env variables.
# Prevents Python from writing pyc files to disc.
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV=${BUILD_ENVIRONMENT}

# Set working directory.
WORKDIR ${APP_HOME}

# Devcontainer dependencies and utils
RUN apt-get update && apt-get install --no-install-recommends -y \
  sudo git bash-completion nano ssh

# Install latest Sqlite for now. Latest Django requires anything above or equals to 3.31
#RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y sqlite3 libsqlite3-dev

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage.
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Use wheels to install python dependencies.
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

# Install dependencies.
RUN pip install --upgrade pip

# copy application code to WORKDIR
COPY . ${APP_HOME}
