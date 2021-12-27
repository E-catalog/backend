from backend.database.db import db_session
from backend.database.individuals_model import Individuals
from flask import jsonify


class SqlIndividualsRepo:

    def get_all(self):
        return db_session.query(Individuals).all()

    def get_by_id(self, id: int):
        return db_session.query(Individuals).get(id)

    def add(self, new_individual: dict) -> dict:
        individual = Individuals(
            name=new_individual['name'],
            place=new_individual['place'],
            sex=new_individual['sex'],
            age=new_individual['age'],
            year_of_excavation=new_individual['year_of_excavation'],
            individual_type=new_individual['individual_type'],
            preservation=new_individual['preservation'],
            epoch=new_individual['epoch'],
            comments=new_individual['comments']
            )

        db_session.add(individual)
        db_session.commit()
        return {
            'message': 'Новый индивид успешно создан'
        }

    def update(self, id: int, update: dict) -> dict:
        individual = db_session.query(Individuals).get(id)

        individual.name = update['name']
        individual.place = update['place']
        individual.sex = update['sex']
        individual.age = update['age']
        individual.year_of_excavation = update['year_of_excavation'],
        individual.individual_type = update['individual_type'],
        individual.preservation = update['preservation'],
        individual.epoch = update['epoch'],
        individual.comments = update['comments']

        db_session.commit()
        return {
            'message': 'Данные индивида успешно обновлены'
        }

    def delete(self, id: int) -> dict:
        individual = db_session.query(Individuals).get(id)
        db_session.delete(individual)
        return {
            'message': f'Индивид {id} удален из базы данных'
        }
