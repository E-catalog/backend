-include .env
export

lint:
	@mypy backend
	@flake8 backend


test:
	@pytest


db.up:
	@docker-compose up -d database


# use reinit to recreate database (remove all data)
db.reinit: db.down db.up


# use after db.reinit with some sleep interval
db.create-tables:
	@python -m backend.database


db.down:
	@echo "clean all resources: db"
	@docker-compose down -t1


run:
	@python -m backend
