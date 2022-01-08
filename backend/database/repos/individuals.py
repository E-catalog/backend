from flask import abort

from backend.database.db import db_session
from backend.database.models.individuals import Individuals


class IndividualsRepo:

    def get_all(self):
        return db_session.query(Individuals).all()

    def get_by_id(self, id: int):
        return db_session.query(Individuals).get(id)

    def add(self, individual) -> dict[str, str]:
        new_individual = Individuals(
            name=individual.name,
            place=individual.place,
            sex=individual.sex,
            age=individual.age,
            year_of_excavation=individual.year_of_excavation,
            individual_type=individual.individual_type,
            preservation=individual.preservation,
            epoch=individual.epoch,
            comments=individual.comments,
        )
        db_session.add(new_individual)
        db_session.commit()
        return {
            'message': 'Новый индивид успешно создан',
        }

    def update(self, id: int, update) -> dict[str, str]:
        individual = db_session.query(Individuals).get(id)

        if individual:
            individual.name = update.name
            individual.place = update.place
            individual.sex = update.sex
            individual.age = update.age
            individual.year_of_excavation = update.year_of_excavation
            individual.individual_type = update.individual_type
            individual.preservation = update.preservation
            individual.epoch = update.epoch
            individual.comments = update.comments

            db_session.commit()
            return {
                'message': 'Данные индивида успешно обновлены',
            }
        else:
            abort(400, 'Такого индивида нет в базе')

    def delete(self, id: int) -> dict[str, str]:
        individual = db_session.query(Individuals).get(id)
        db_session.delete(individual)
        return {
            'message': f'Индивид {id} удален из базы данных',
        }
