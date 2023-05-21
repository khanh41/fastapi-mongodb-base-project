
FROM python:3.10.11-slim

ENV PYTHONUNBUFFERED 1
ENV DIRECTORY {{cookiecutter.project_slug}}
EXPOSE 8088
WORKDIR /app/$DIRECTORY

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* .venv venv

COPY $DIRECTORY/pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.in-project false && \
    poetry install --no-dev

COPY ./$DIRECTORY ./

CMD poetry run uvicorn --host=0.0.0.0 --port 8088 app.main:app
