# Backend

# Contributing
Since this is a young Python project, we assume that you're already have Python >=3.6 in your system.

### Docker
We use Docker containers to store different services of our project.
Docker Compose manages all of these stuff for us.
Therefore we advise to install Docker Desktop on your machine (use link https://www.docker.com/products/docker-desktop).

This repository already has the *docker-compose.yml* file with instructions for Docker Compose. All you need is to create an *.env* file in the root directory and set environmental variables. Use *.env.default* as a template for this.

:exclamation: *.env* file will contain your personal data (keys, passwords, tokens, etc). Don't forget to add it in the .gitignore - do not share this info with the hole world.

To run the intire app with the Docker Compose use
```
    docker compose up
```
Alternatively, you may use `docker-compose up` and run the app using docker-compose binary.

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
This repository already has *poetry.lock* and *pyproject.toml* files, so you simply install all dependencies by a single command:
```
    poetry install
```
Ta-dam! Now you have all you need to start.

### Run app:
To run the project in the terminal use
```
    python -m backend
```
