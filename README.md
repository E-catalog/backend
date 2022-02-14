# Backend

## About

This application is a backend of our E-catalog project. It runs independently and connects to the database at one end and to the frontend app - at other end. All connections are made via the http protocol.

The main function of this application is to trasfer data between database and the one who asks. You can get or push data from/to the database through our API and simple CRUD operations. They are similar for two basic instanses - Places and Individuals:

```
# get all places
GET api/v1/places/

# get a particular place
GET api/v1/places/<uid>

# create a place
POST api/v1/places/

# update a particular place
PUT api/v1/places/<uid>

# delete a particular place
DELETE api/v1/places/<uid>

# get all individuals
GET api/v1/individuals

# get a particular individual
GET api/v1/individuals/<uid>

# create an individual
POST api/v1/individuals/

# update a particular individual
PUT api/v1/individuals/<uid>

# delete a particular individual
DELETE api/v1/individuals/<uid>
```

## Contributing

Since this is a young Python project, we assume that you already have Python >=3.6 in your system. Clone this repository to your machine and follow the instructions.

### Docker

We use Docker containers to store different services of our project.
Docker Compose manages all of these stuff for us.
Therefore we advise to install Docker Desktop on your machine (use [link](https://www.docker.com/products/docker-desktop)).

This repository already has the *docker-compose.yml* file with instructions for Docker Compose. All you need is to create an *.env* file in the root directory and set environmental variables. Use *.env.default* as a template for this.

:exclamation: *.env* file will contain your personal data (keys, passwords, tokens, etc). Don't forget to add it in the *.gitignore* - do not share this info with the hole world.

To run the entire app with the Docker Compose use

```bash, PowerShell, CMD
    docker compose up -d
```

Alternatively, you may use `docker-compose up` and run the app using docker-compose binary. The `-d` or `--detach` flag is used to run containers in the background, so your terminal stays free for other actions.

To run a specific container

```bash, PowerShell, CMD
    docker compose run -d <container_name>
```

To stop the entire app use

```bash, PowerShell, CMD
    docker-compose stop -t1
```

Or type the name of the container to stop only this container. The `-t1` flag sets the stopping time to 1 sec. By default this value is 10 sec.

To shut down the entire app use

```bash, PowerShell, CMD
    docker compose down
```

:exclamation: Note that at the current stage of development this command will erase the hole database from the container (because it exists only there for now). So you should initiate and fill the database again when starting the app.

### Install requirements

First of all, we're using Poetry to manage dependencies (and to make our lives easier too).

Install Poetry (globally):

```bash, PowerShell, CMD
    pip install poetry
```

Than you should create a virtual environment (.venv) in the root directory of your project

```bash, PowerShell, CMD
    poetry config virtualenvs.in-project true
```

This repository already has *poetry.lock* and *pyproject.toml* files, so you simply install all dependencies by a single command:

```bash, PowerShell, CMD
    poetry install
```

:exclamation: Note that Poetry will install all dependencies in the project virtual environment. It means you won't be able to use them outside it.
To run any file or package inside the Poetry environment use `poetry run <name_of_file_or_package>`

Ta-dam! Now you have all you need to start.

### Run app

To run the project in the terminal use

```bash, PowerShell, CMD
    poetry run python -m backend
```

Or you can use 'Run and Debug' if you're using VS Code - the necessary *launch.json* file are already there. Use 'service' to run the app and 'create_table' to create database's tables.

### Using linters

We use **wemake-python-styleguide** - "the strictest and most opinionated Python linter ever". Actually it's just a **flake8** plugin with some other useful plugins. Poetry files already have all dependencies, so you'll have the hole package of the linter after runnig `poetry install`.

To check the hole app code run

```bash, PowerShell, CMD
    poetry run flake8 backend
    poetry run mypy backend
```

It will examine all python files in *backend* directory.
If you want to check any particular python file simply use `poetry run flake8 <path/file_name>` or the same for **mypy**.
