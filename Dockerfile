FROM python:3.12-slim AS builder
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1

# to run poetry directly as soon as it's installed
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install poetry and clear cache
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# copy only pyproject.toml and poetry.lock file nothing else here

COPY poetry.lock pyproject.toml ./
# this will create the folder /app/.venv (might need adjustment depending on which poetry version you are using)
# Install dependencies

RUN poetry install --no-dev --no-interaction --no-ansi
# ---------------------------------------------------------------------

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

RUN useradd -m userbackend

WORKDIR /app

# copy the venv folder from builder image
COPY --from=builder /app/.venv ./.venv

RUN chown -R userbackend:userbackend /app

USER userbackend

COPY src ./src

ENV PYTHONPATH /app/src

EXPOSE 8000

CMD ["fastapi", "dev", "main.py"]