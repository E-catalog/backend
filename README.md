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

:exclamation: Note that Poetry will install all dependencies in the project virtual environment. It means you won't be able to use them outside it.
To run any file or package inside the Poetry environment use `poetry run <name_of_file_or_package>`

Ta-dam! Now you have all you need to start.

### Run app:
To run the project in the terminal use
```
    python -m backend
```

### Using linter
We use **wemake-python-styleguide** - "the strictest and most opinionated Python linter ever". Actually it's just a **flake8** plugin with some other useful plugins. Poetry files already have all dependencies, so you'll have the hole package of the linter after runnig `poetry install`.

To check the project code run
```
    poetry run flake8 backend
```
It will examine all python files in *backend* directory.
If you want to check any particular python file simply use `poetry run flake8 <path/file_name>`.
