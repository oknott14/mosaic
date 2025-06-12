FROM ghcr.io/astral-sh/uv:python3.12-alpine AS development

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY /apps/node/pyproject.toml pyproject.toml
COPY apps/node/uv.lock uv.lock

RUN uv sync --locked

COPY apps/node/main.py main.py
COPY apps/node/manage.py manage.py
COPY apps/node/node node

CMD ["uv", "run",  "manage.py",  "runserver", "0.0.0.0:3000"]

