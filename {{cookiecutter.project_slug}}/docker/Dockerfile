FROM python:3.10

ENV PYTHONUNBUFFERED 1

EXPOSE {{cookiecutter.port}}
WORKDIR /app

RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get install ffmpeg libsm6 libxext6  -y && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* .venv

RUN apt-get update && \
    apt-get install python3 python3-pip build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev -y

RUN pip install poetry && \
    poetry config virtualenvs.in-project false

COPY pyproject.toml ./

RUN poetry install --no-dev

COPY . ./

RUN poetry run pytest -v

CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "{{cookiecutter.port}}"]
