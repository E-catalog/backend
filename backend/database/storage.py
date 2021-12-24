from backend.database.db import db_session
from backend.database.individuals_model import Individuals
from flask import jsonify


class SqlIndividualsRepo:

    def get_all(self):
        all_individuals = db_session.query(Individuals).all()
        return jsonify(all_individuals)

    def get_by_id(self, id: int):
        individual = db_session.query(Individuals).filter(Individuals.id == id).one()
        return individual

    def add(self, new_individual: dict) -> None:
        individual = Individuals(
            name=new_individual['name'],
            place=new_individual['place'],
            sex=new_individual['sex'],
            age=new_individual['age'])
        db_session.add(individual)
        db_session.commit()

    def update(self, id: int, update: dict) -> None:
        individual = db_session.query(Individuals).filter(Individuals.id == id).one()
        individual.name = update['name']
        individual.place = update['place']
        individual.sex = update['sex']
        individual.age = update['age']
        db_session.commit()

    def delete(self, id: int) -> None:
        individual = db_session.query(Individuals).filter(Individuals.id == id).one()
        db_session.delete(individual)
