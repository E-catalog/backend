import logging
from http import HTTPStatus
from typing import TypeVar

from flask import Flask, abort, jsonify, request
from pydantic import BaseModel, ValidationError
from werkzeug.exceptions import BadRequest, InternalServerError, MethodNotAllowed, NotFound

from backend.repos.individuals import IndividualsRepo
from backend.repos.places import PlacesRepo
from backend.schemas import Individual, Place

app = Flask(__name__)
individuals_repo = IndividualsRepo()
places_repo = PlacesRepo()
logger = logging.getLogger(__name__)

TC = TypeVar('TC', bound=BaseModel)


def to_json(items: list[TC]):
    return jsonify([item.dict() for item in items])


def handle_bad_request(error: BadRequest):
    return {'error': 'Bad request'}, 400


def handle_not_found(error: NotFound):
    return {'error': 'Not found'}, 404


def handle_method_not_allowed(error: MethodNotAllowed):
    return {'error': 'Method not allowed'}, 405


def handle_internal_server_error(error: InternalServerError):
    return {'error': 'Internal server error'}, 500


app.register_error_handler(BadRequest, handle_bad_request)
app.register_error_handler(NotFound, handle_not_found)
app.register_error_handler(MethodNotAllowed, handle_method_not_allowed)
app.register_error_handler(InternalServerError, handle_internal_server_error)


@app.route('/api/v1/individuals/', methods=['GET'])
def get_all_individuals():
    all_individuals = individuals_repo.get_all()
    return jsonify(all_individuals), 200


@app.route('/api/v1/places/', methods=['GET'])
def get_all_places():
    entities = places_repo.get_all()
    places = [Place.from_orm(place) for place in entities]
    return to_json(places), 200


@app.route('/api/v1/individuals/<int:uid>', methods=['GET'])
def get_individual(uid):
    entity = individuals_repo.get_by_uid(uid)
    individual = Individual.from_orm(entity)
    return individual.dict(), 200


@app.route('/api/v1/places/<int:uid>', methods=['GET'])
def get_place(uid):
    place = places_repo.get_by_id(uid)
    return Place.from_orm(place).dict(), 200


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


@app.route('/api/v1/places/', methods=['POST'])
def create_place():
    data = request.json
    if not data:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    try:
        place = Place(**data)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации места: %s', error)
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    entity = places_repo.add(
        name=place.name,
        head_of_excavations=place.head_of_excavations,
        type_of_burial_site=place.type_of_burial_site,
        coordinates=place.coordinates,
        comments=place.comments,
    )
    new_place = Place.from_orm(entity)
    return new_place.dict(), 201


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

    update = individuals_repo.update(
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
    return update, 200


@app.route('/api/v1/places/<int:uid>', methods=['PUT'])
def update_place(uid):
    payload = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    try:
        place = Place(**payload)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации места: %s', error)
        abort(HTTPStatus.BAD_REQUEST, 'Неверный тип данных в запросе')

    entity = places_repo.update(
        uid=uid,
        name=place.name,
        head_of_excavations=place.head_of_excavations,
        type_of_burial_site=place.type_of_burial_site,
        coordinates=place.coordinates,
        comments=place.comments,
    )
    updated_place = Place.from_orm(entity)
    return updated_place.dict(), 200


@app.route('/api/v1/individuals/<int:uid>', methods=['DELETE'])
def del_individual(uid):
    individuals_repo.delete(uid)
    return {}, 204


@app.route('/api/v1/places/<int:uid>', methods=['DELETE'])
def del_place(uid):
    places_repo.delete(uid)
    return {}, 204
