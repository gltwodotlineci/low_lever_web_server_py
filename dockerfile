FROM python:3.8-bullseye

## UPDATE
RUN apt-get update && apt-get upgrade -y

## POSTGRES CLIENT
RUN mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7 \
    && apt-get install -y --no-install-recommends postgresql-client

RUN apt-get install -y nano iputils-ping curl borgbackup cron gettext

# Create user and switch to it in the same RUN command, setting PATH correctly
RUN useradd -ms /bin/bash admin_server && exec su -l admin_server
USER admin_server

## PYTHON
RUN curl -sSL https://install.python-poetry.org | python3 -
# Update PATH to include Poetry
ENV PATH="/home/admin_server/.local/bin:$PATH"


# Copy the project files into the container
COPY ./ /server_low_leverl_py
# Set the working directory
WORKDIR /server_low_leverl_py

# Install poetry
#RUN poetry install

