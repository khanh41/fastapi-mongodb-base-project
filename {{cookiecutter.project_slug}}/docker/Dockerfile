FROM python:3.7.11

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

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.in-project false && \
    poetry install --no-dev

COPY . ./

RUN poetry run python run_crontab.py
CMD ["poetry", "run","uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "{{cookiecutter.port}}"]
