from flask import Flask, json, request, jsonify
from werkzeug.exceptions import InternalServerError, MethodNotAllowed, NotFound, HTTPException
#from backend.database.fake_storage import IndividualsRepo
from backend.database.storage import SqlIndividualsRepo


errors = {
    404: {'error': '404', 'message': 'Not found'},
    405: {'error': '405', 'message': 'Method not allowed'},
    500: {'error': '500', 'message': 'Internal server error'}
}

places = {
    "id": 5,
    "title": "Мамаев Курган",
    "category": "Курган",
}

app = Flask(__name__)
individuals_repo = SqlIndividualsRepo()


def handle_404(e):
    return errors[404], 404


def handle_405(e):
    return errors[405], 405


def handle_500(e):
    return errors[500], 500


def handle_nothttp_exception(e):
    if not isinstance(e, HTTPException):
        return errors[500], 500


app.register_error_handler(NotFound, handle_404)
app.register_error_handler(MethodNotAllowed, handle_405)
app.register_error_handler(InternalServerError, handle_500)
#app.register_error_handler(Exception, handle_nothttp_exception)


def convert_from_object(sql_individual):
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
        'year_of_excavation': sql_individual.year_of_excavation
    }


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    response = individuals_repo.get_all()
    individuals = [convert_from_object(ind) for ind in response]
    return jsonify(individuals), 200


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    individual = convert_from_object(individuals_repo.get_by_id(individual_id))
    return jsonify(individual), 200


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    return individuals_repo.add(request.json), 201


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def update_individual(individual_id):
    return individuals_repo.update(individual_id, request.json), 200


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    return individuals_repo.delete(individual_id), 200


@app.route("/api/v1/places/<int:place_id>", methods=['GET'])
def get_place(place_id: int):
    return places[place_id]


@app.route("/api/v1/places/", methods=['POST'])
def create_places():
    new_id = max(places) + 1
    places[new_id] = {
        "id": new_id,
        "title": request.json['title'],
        "category": request.json['category']
        }
    return places[new_id], 201


@app.route("/api/v1/places/<int:places_id>", methods=['DELETE'])
def del_places(places_id):
    del places[places_id]
    return {}, 204


@app.route("/api/v1/places/<int:places_id>", methods=['PUT'])
def change_places(places_id):
    places =places[places_id]
    places ['title'] = request.json.get('title',  places['title'])
    places ['category'] = request.json.get('category', places['category'])
    return places

