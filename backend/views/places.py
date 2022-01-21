import logging
from http import HTTPStatus
from typing import TypeVar

from flask import Blueprint, abort, jsonify, request
from pydantic import BaseModel, ValidationError

from backend.app import app
from backend.repos.places import PlacesRepo
from backend.schemas import Place

routes = Blueprint('places', __name__)
places_repo = PlacesRepo()
logger = logging.getLogger(__name__)
TC = TypeVar('TC', bound=BaseModel)


def to_json(items: list[TC]):
    return jsonify([item.dict() for item in items])


@app.route('/api/v1/places/', methods=['GET'])
def get_all_places():
    entities = places_repo.get_all()
    places = [Place.from_orm(place) for place in entities]
    return to_json(places), HTTPStatus.OK


@app.route('/api/v1/places/<int:uid>', methods=['GET'])
def get_place(uid):
    place = places_repo.get_by_id(uid)
    if not place:
        abort(HTTPStatus.NOT_FOUND, 'Place not found')

    return Place.from_orm(place).dict(), HTTPStatus.OK


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
    return new_place.dict(), HTTPStatus.CREATED


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
    return updated_place.dict(), HTTPStatus.OK


@app.route('/api/v1/places/<int:uid>', methods=['DELETE'])
def del_place(uid):
    places_repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
