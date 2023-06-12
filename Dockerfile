FROM python:3.11

RUN apt-get update
RUN pip install poetry

RUN touch .env
ENV APP_DIR /usr/src/app/
WORKDIR ${APP_DIR}

COPY poetry.toml pyproject.toml poetry.lock ${APP_DIR}
RUN poetry install --no-interaction --no-ansi -vvv

COPY . ${APP_DIR}
RUN chmod 0700 ./entrypoint.sh

EXPOSE 8000
CMD ["sh", "entrypoint.sh"]
