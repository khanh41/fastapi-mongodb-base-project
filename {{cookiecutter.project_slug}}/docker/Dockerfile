FROM python:3.11.6 as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update &&  \
    apt-get install --no-install-recommends -y curl build-essential

FROM python-base as builder-base

RUN curl -sSL https://install.python-poetry.org | python

WORKDIR $PYSETUP_PATH
COPY pyproject.toml ./

RUN poetry install

FROM python-base as development
ENV FASTAPI_ENV=development

EXPOSE 8088

WORKDIR $PYSETUP_PATH

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY . /app/
WORKDIR /app

RUN poetry run pytest -v

CMD ["hypercorn", "app.main:app", "--worker-class", "trio", "--bind", "0.0.0.0:8088", "--workers", "4"]

FROM python-base as production
ENV FASTAPI_ENV=production

EXPOSE 8088

WORKDIR $PYSETUP_PATH

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY . /app/
WORKDIR /app

RUN poetry run pytest -v

CMD ["hypercorn", "app.main:app", "--worker-class", "trio", "--bind", "0.0.0.0:{{cookiecutter.port}}", "--workers", "8"]
