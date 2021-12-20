# Backend

# Contributing
Since this is a young Python project, we assume that you're already have Python >=3.6 in your system.

### Install requirements
First of all, we're using Poetry to manage dependencies (and to make our lives easier too).

Install Poetry (globally):
```
    pip install poetry
```
Than you should create a virtual environment (.venv) in the root directory of your project
```
    poetry config virtualenvs.in-project true
```
This repository already has poetry.lock and pyproject.toml files, so you simply install all dependencies by a single command:
```
    poetry install
```
Ta-dam! Now you have all you need to start.

### Run app:
To run the project in the terminal use
```
    python -m backend
```
