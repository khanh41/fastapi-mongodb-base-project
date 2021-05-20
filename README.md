# Base code
---
## Preview 🌄
![ui](https://i.imgur.com/euRQPZU.png)

---

![swagger](https://i.imgur.com/6yOyBaa.png)

## Installation ⚡️
### Requires
- Python: 3.7~3.8

Install with poetry:
~~~
pip install poetry
poetry install
~~~

## Deployment app ⛄️
Clone:
~~~
git clone https://gitlab-new.bap.jp/AI-KEIBA/keiba-ai-system.git
~~~
Run MongoDB with docker:
~~~
sudo docker pull mongo
sudo docker run --name some-mongo -p 27017:27017 -d mongo
~~~

Run fastapi with poetry:
~~~
poetry run uvicorn --host=0.0.0.0 --port 8088 app.main:app
> Uvicorn running on http://0.0.0.0:8088 (Press CTRL+C to quit)
~~~

Run crontab to schedule: with `-n` or `--number` is number minutes wait for schedule, 0 to stop
~~~
poetry run python run_crontab.py -n 1
~~~

## Deployment with Docker 🐳
Docker build and run with Dockerfile:
~~~
sudo docker pull mongo
sudo docker run --name some-mongo -p 27017:27017 -d mongo
sudo docker build -t keiba .
sudo docker run -it -d keiba
~~~
Deployment with docker-compose: 
~~~
docker-compose up -d
~~~
- Server backend - docs: http://0.0.0.0:8088/docs
- Api backend: http://0.0.0.0:8088/redoc
- Server frontend: http://0.0.0.0:8088

## Run tests 😋
Tests for this project are defined in the `tests/` folder.
~~~
pytest
~~~

## Run tools 🌍
Auto format: 
~~~
poetry run app/utils/format
~~~

Auto lint: 
~~~
poetry run app/utils/lint
~~~

Auto test: 
~~~
poetry run app/utils/test
~~~

## Tree directory 🌗 
~~~
app
├── api                  - web related stuff.
│   ├── database         - config database.
│   │   ├── models       - definition of error handlers.
│   │   ├── excute       - sql handling, CRUD.
│   │   ├── connect.py   - connect to database.
│   ├── errors           - definition of error handlers.
│   └── routes           - web routes.
│   └── services         - logic that is not just crud related.
│   └── responses        - response for api request corresponding.
├── ml                   - machine learning model and preprocessing.
│   ├── data_loader      - load data or model.
│   ├── preprocessing    - preprocessing data.
│   ├── figures          - draw (ignore).
│   ├── metrics          - metrics for model, etc.
│   ├── base_model       - model machine learning setup
│   ├── trainers         - model machine learning training.
├── core                 - application configuration, startup events, logging.
├── logger               - export log for server process.
├── tests                - test api, code.
├── utils                - tools format, lint, test, etc.
├── resources            - image, audio, csv, etc. (ignore)
├── pyproject.toml       - dependencies and package.
└── main.py              - FastAPI application creation and configuration.
~~~
