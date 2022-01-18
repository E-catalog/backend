from http import HTTPStatus
from typing import Any

from flask import abort

from backend.database.models import Individuals
from backend.database.session import db_session


class IndividualsRepo:

    def get_all(self) -> list[dict[str, Any]]:
        all_individuals = db_session.query(Individuals).all()
        return [ind.to_dict() for ind in all_individuals]

    def get_by_uid(self, uid: int) -> dict[str, Any]:
        individual = db_session.query(Individuals).get(uid)
        return individual.to_dict()

    def add(self, individual: dict[str, Any]) -> dict[str, Any]:
        new_individual = Individuals(
            name=individual['name'],
            place_uid=individual['place_uid'],
            sex=individual['sex'],
            age=individual['age'],
            year_of_excavation=individual['year_of_excavation'],
            individual_type=individual['individual_type'],
            preservation=individual['preservation'],
            epoch=individual['epoch'],
            comments=individual['comments'],
        )
        db_session.add(new_individual)
        db_session.commit()
        return new_individual.to_dict()

    def update(self, uid: int, update: dict[str, Any]) -> dict[str, Any]:
        individual = db_session.query(Individuals).get(uid)

        if not individual:
            abort(HTTPStatus.BAD_REQUEST, 'Такого индивида нет в базе')

        individual.name = update['name']
        individual.place_uid = update['place_uid']
        individual.sex = update['sex']
        individual.age = update['age']
        individual.year_of_excavation = update['year_of_excavation']
        individual.individual_type = update['individual_type']
        individual.preservation = update['preservation']
        individual.epoch = update['epoch']
        individual.comments = update['comments']

        db_session.commit()
        return individual.to_dict()

    def delete(self, uid: int) -> None:
        individual = db_session.query(Individuals).get(uid)
        db_session.delete(individual)
        db_session.commit()
