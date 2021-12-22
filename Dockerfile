FROM python:3.9-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY backend /app/backend

CMD ["poetry", "run", "python", "-m", "backend"]
