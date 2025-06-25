FROM ghcr.io/astral-sh/uv:python3.12-alpine AS development

# Accept build argument
ARG API_PORT=3000
ARG API_HOST=0.0.0.0

ENV PORT=$API_PORT
ENV HOST=$API_HOST

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY /apps/node/ .

RUN uv sync

CMD uv run fastapi dev main.py --port ${PORT} --host ${HOST}
