import logging
from typing import Optional

from flask import Flask, abort, jsonify, request
from pydantic import BaseModel, ValidationError
from werkzeug.exceptions import BadRequest, InternalServerError, MethodNotAllowed, NotFound

from backend.database.repos.individuals import IndividualsRepo
from backend.database.repos.places import PlacesRepo

app = Flask(__name__)
individuals_repo = IndividualsRepo()
places_repo = PlacesRepo()
logger = logging.getLogger(__name__)

errors = {
    'BadRequest': {'error': '400', 'message': 'Bad request'},
    'NotFound': {'error': '404', 'message': 'Not found'},
    'MethodNotAllowed': {'error': '405', 'message': 'Method not allowed'},
    'InernalServerError': {'error': '500', 'message': 'Internal server error'},
}


def handle_bad_request(error):
    return errors['BadRequest'], 400


def handle_not_found(error: NotFound):
    return errors['NotFound'], 404


def handle_method_not_allowed(error):
    return errors['MethodNotAllowed'], 405


def handle_internal_server_error(error):
    return errors['InernalServerError'], 500


app.register_error_handler(BadRequest, handle_bad_request)
app.register_error_handler(NotFound, handle_not_found)
app.register_error_handler(MethodNotAllowed, handle_method_not_allowed)
app.register_error_handler(InternalServerError, handle_internal_server_error)


class Individual(BaseModel):
    name: str
    place: str
    year_of_excavation: Optional[int]
    sex: Optional[str]
    age: Optional[str]
    individual_type: Optional[str]
    preservation: Optional[str]
    epoch: Optional[str]
    comments: Optional[str]


def converter(sql_individual):
    return {
        'id': sql_individual.id,
        'name': sql_individual.name,
        'place': sql_individual.place,
        'sex': sql_individual.sex,
        'age': sql_individual.age,
        'individual_type': sql_individual.individual_type,
        'preservation': sql_individual.preservation,
        'epoch': sql_individual.epoch,
        'comments': sql_individual.comments,
        'year_of_excavation': sql_individual.year_of_excavation,
    }


@app.route('/api/v1/individuals/', methods=['GET'])
def get_all_individuals():
    response = individuals_repo.get_all()
    individuals = [converter(ind) for ind in response]
    return jsonify(individuals), 200


@app.route('/api/v1/places/', methods=['GET'])
def get_all_places():
    return places_repo.get_all()


@app.route('/api/v1/individuals/<int:individual_id>', methods=['GET'])
def get_individual(individual_id):
    individual = converter(individuals_repo.get_by_id(individual_id))
    return jsonify(individual), 200


@app.route('/api/v1/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    return places_repo.get_by_id(place_id)


@app.route('/api/v1/individuals/', methods=['POST'])
def create_individual():
    payload = request.json
    if not payload:
        abort(400, 'Тело запроса не может быть пустым')

    try:
        individual = Individual(**payload)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации: %s', error)
        abort(400, 'Неверный тип данных в запросе')

    return individuals_repo.add(individual), 201


@app.route('/api/v1/places/', methods=['POST'])
def create_place():
    data = request.json
    if data:
        new_place = {
            'title': data['title'],
            'category': data['category'],
        }
        return places_repo.add(new_place)
    else:
        abort(400, 'Тело запроса не может быть пустым')


@app.route('/api/v1/individuals/<int:individual_id>', methods=['PUT'])
def update_individual(individual_id):
    payload = request.json
    if not payload:
        abort(400, 'Тело запроса не может быть пустым')

    try:
        individual = Individual(**payload)
    except ValidationError as error:
        logger.info('Ошибка в процессе pydantic-валидации: %s', error)
        abort(400, 'Неверный тип данных в запросе')

    return individuals_repo.update(individual_id, individual), 200


@app.route('/api/v1/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json
    if data:
        updates = {
            'title': data['title'],
            'category': data['category'],
        }
        return places_repo.update(place_id, updates)
    else:
        abort(400, 'Тело запроса не может быть пустым')


@app.route('/api/v1/individuals/<int:individual_id>', methods=['DELETE'])
def del_individual(individual_id):
    return individuals_repo.delete(individual_id), 200


@app.route('/api/v1/places/<int:place_id>', methods=['DELETE'])
def del_place(place_id):
    return places_repo.delete(place_id)
