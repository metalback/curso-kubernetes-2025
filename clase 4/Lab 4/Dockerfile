FROM python:3.12 

WORKDIR /code 

ARG BASE_PATH=.

COPY $BASE_PATH/openssl.cnf /etc/ssl/openssl.cnf

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN sh -c "curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -" \
    && apt-get update \
    && sh -c "curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list" \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN apt-get install unixodbc

COPY $BASE_PATH/pyproject.toml $BASE_PATH/poetry.lock* /code/

ENV PYTHONPATH=/code

COPY $BASE_PATH/app /code/app

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

COPY app ./app
