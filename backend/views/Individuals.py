import logging
from http import HTTPStatus
from typing import TypeVar

from flask import Blueprint, abort, jsonify, request
from pydantic import BaseModel, ValidationError

from backend.app import app
from backend.repos.individuals import IndividualsRepo
from backend.repos.places import PlacesRepo
from backend.schemas import Individual


individuals_repo = IndividualsRepo()
places_repo = PlacesRepo()
logger = logging.getLogger(__name__)
TC = TypeVar('TC', bound=BaseModel)


def to_json(items: list[TC]):
    return jsonify([item.dict() for item in items])


@app.route('/api/v1/individuals/', methods=['GET'])
def get_all_individuals():
    places = {place.uid: Place.from_orm(place) for place in places_repo.get_all()}
    entities = individuals_repo.get_all()
    individuals = [Individual.from_orm(entity) for entity in entities]

    for individual in individuals:
        individual.links['place'] = places.get(individual.place_uid)

    return to_json(individuals), 200


@app.route('/api/v1/individuals/<int:uid>', methods=['GET'])
def get_individual(uid):
    entity = individuals_repo.get_by_uid(uid)
    if not entity:
        abort(HTTPStatus.NOT_FOUND, 'Individual not found')

    individual = Individual.from_orm(entity)
    place_entity = places_repo.get_by_id(individual.place_uid)
    individual.links['place'] = Place.from_orm(place_entity)
    return individual.dict(), HTTPStatus.OK


@app.route('/api/v1/individuals/', methods=['POST'])
def create_individual():
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    try:
        individual = Individual(**payload)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации индивида: %s', error)
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    entity = individuals_repo.add(
        name=individual.name,
        place_id=individual.place_uid,
        year_of_excavation=individual.year_of_excavation,
        sex=individual.sex,
        age=individual.age,
        individual_type=individual.individual_type,
        preservation=individual.preservation,
        epoch=individual.epoch,
        comments=individual.comments,
    )
    individual = Individual.from_orm(entity)
    return individual.dict(), 201


@app.route('/api/v1/individuals/<int:uid>', methods=['PUT'])
def update_individual(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    try:
        individual = Individual(**payload)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации: %s', error)
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    entity = individuals_repo.update(
        uid=uid,
        name=individual.name,
        place_id=individual.place_uid,
        year_of_excavation=individual.year_of_excavation,
        sex=individual.sex,
        age=individual.age,
        individual_type=individual.individual_type,
        preservation=individual.preservation,
        epoch=individual.epoch,
        comments=individual.comments,
    )
    return Individual.from_orm(entity).dict(), 200


@app.route('/api/v1/individuals/<int:uid>', methods=['DELETE'])
def del_individual(uid):
    individuals_repo.delete(uid)
    return {}, 204