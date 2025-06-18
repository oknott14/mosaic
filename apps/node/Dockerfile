FROM ghcr.io/astral-sh/uv:python3.12-alpine AS development
RUN apt-get update -yq && apt-get install -yqq curl

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY /apps/node/pyproject.toml pyproject.toml
COPY apps/node/uv.lock uv.lock
COPY apps/node/manage.py manage.py
COPY apps/node/node node
COPY apps/node/db.sqlite3 db.sqlite3

RUN uv sync
ENV PATH="/usr/src/app/.venv/bin:$PATH"
RUN uv run manage.py migrate

CMD ["uv", "run",  "manage.py",  "runserver", "0.0.0.0:3000"]

