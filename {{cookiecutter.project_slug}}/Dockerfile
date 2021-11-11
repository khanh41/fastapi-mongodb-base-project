
FROM python:3.8.1-slim

ENV PYTHONUNBUFFERED 1

EXPOSE {{cookiecutter.port}}
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* .venv venv

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.1 && \
    poetry config virtualenvs.in-project false && \
    poetry install --no-dev

COPY . ./

RUN poetry run python run_crontab.py
CMD poetry run uvicorn --host={{cookiecutter.host}} --port {{cookiecutter.port}} app.main:app
