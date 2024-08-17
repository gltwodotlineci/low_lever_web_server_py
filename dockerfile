FROM python:3.8-bullseye

## UPDATE
RUN apt-get update && apt-get upgrade -y

## POSTGRES CLIENT
RUN mkdir -p /usr/share/man/man1
RUN mkdir -p /usr/share/man/man7
RUN apt-get install -y --no-install-recommends postgresql-client

RUN apt-get install -y nano iputils-ping curl borgbackup cron gettext

RUN useradd -ms /bin/bash tibillet
USER glen

#ENV POETRY_NO_INTERACTION=1

## PYTHON
#RUN curl -sSL https://install.python-poetry.org | python3 -
#ENV PATH=".local/bin:$PATH"

WORKDIR /DjangoFiles
#RUN poetry install
#RUN poetry update

