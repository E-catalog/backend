from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException, InternalServerError, MethodNotAllowed, NotFound
from werkzeug.wrappers import response
from backend.database.models import places
from backend.database.repos.individuals import IndividualsRepo
from backend.database.repos.places import PlacesRepo
from pydantic import BaseModel, ValidationError
from typing import Optional


errors = {
    'NotFound': {'error': '404', 'message': 'Not found'},
    'MethodNotAllowed': {'error': '405', 'message': 'Method not allowed'},
    'InernalServerError': {'error': '500', 'message': 'Internal server error'},
}

app = Flask(__name__)
individuals_repo = IndividualsRepo()
places_repo = PlacesRepo()


def handle_not_found(error):
    return errors['NotFound'], 404


def handle_method_not_allowed(error):
    return errors['MethodNotAllowed'], 405


def handle_internal_server_error(error):
    return errors['InernalServerError'], 500


def handle_nothttp_exception(error):
    if not isinstance(error, HTTPException):
        return errors['InternalServerError'], 500


app.register_error_handler(NotFound, handle_not_found)
app.register_error_handler(MethodNotAllowed, handle_method_not_allowed)
app.register_error_handler(InternalServerError, handle_internal_server_error)
app.register_error_handler(Exception, handle_nothttp_exception)


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

class Places(BaseModel):
    name: str
    head_of_excavations: Optional[str]
    type_of_burial_site:   Optional[str]
    coordinates:   Optional[str]
    comments:   Optional[str]


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

def converterr(sql_places):
    return {
        'id': sql_places.id,
        'name': sql_places.name,
        'head_of_excavations': sql_places.head_of_excavations,
        'type_of_burial_site': sql_places.type_of_burial_site,
        'comments': sql_places.comments,
        'coordinates': sql_places.coordinates,
        }



@app.route('/api/v1/individuals/', methods=['GET'])
def get_all_individuals():
    response = individuals_repo.get_all()
    individuals = [converter(ind) for ind in response]
    return jsonify(individuals), 200


@app.route('/api/v1/places/', methods=['GET'])
def get_all_places():
    response = places_repo.get_all()
    places = [converter(ind) for ind in response]
    return jsonify(places), 200


@app.route('/api/v1/individuals/<int:individual_id>', methods=['GET'])
def get_individual(individual_id):
    individual = converter(individuals_repo.get_by_id(individual_id))
    return jsonify(individual), 200


@app.route('/api/v1/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = converter(places_repo.get_by_id(place_id))
    return jsonify(place), 200


@app.route('/api/v1/individuals/', methods=['POST'])
def create_individual():
    payload = request.json
    try:
        individual = Individual(**payload)
    except ValidationError as error:
        print(error)
    return individuals_repo.add(individual), 201


@app.route('/api/v1/places/', methods=['POST'])
def create_place():
    payload = request.json
    try:
        place = Places(**payload)
    except ValidationError as error:
        print(error)
    return places_repo.add(place), 201


@app.route('/api/v1/individuals/<int:individual_id>', methods=['PUT'])
def update_individual(individual_id):
    payload = request.json
    try:
        individual = Individual(**payload)
    except ValidationError as error:
        print(error)
    return individuals_repo.update(individual_id, individual), 200


@app.route('/api/v1/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    payload = request.json
    try:
        place = Places(**payload)
    except ValidationError as error:
        print(error)
    return places_repo.update(place_id, place), 200


@app.route('/api/v1/individuals/<int:individual_id>', methods=['DELETE'])
def del_individual(individual_id):
    return individuals_repo.delete(individual_id), 200


@app.route('/api/v1/places/<int:place_id>', methods=['DELETE'])
def del_place(place_id):
    return places_repo.delete(place_id)
