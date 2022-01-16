from http import HTTPStatus

from flask import abort

from backend.database.models import Individuals
from backend.database.session import db_session


class IndividualsRepo:

    def get_all(self):
        return db_session.query(Individuals).all()

    def get_by_uid(self, uid: int):
        return db_session.query(Individuals).get(uid)

    def add(self, individual) -> dict[str, str]:
        new_individual = Individuals(
            name=individual.name,
            place_uid=individual.place_uid,
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

    def update(self, uid: int, update) -> dict[str, str]:
        individual = db_session.query(Individuals).get(uid)

        if not individual:
            abort(HTTPStatus.BAD_REQUEST, 'Такого индивида нет в базе')

        individual.name = update.name
        individual.place_uid = update.place_uid
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

    def delete(self, uid: int) -> dict[str, str]:
        individual = db_session.query(Individuals).get(uid)
        db_session.delete(individual)
        db_session.commit()
        return {
            'message': f'Индивид {uid} удален из базы данных',
        }
