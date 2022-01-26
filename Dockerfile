FROM python:3.9-slim

ENV PYTHONUNBUFFERED=True \
    POETRY_VIRTUALENVS_CREATE=False

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY backend /app/backend

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "backend.app:app"]
