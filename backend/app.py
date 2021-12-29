from flask import Flask, json, request, jsonify
from werkzeug.exceptions import InternalServerError, MethodNotAllowed, NotFound, HTTPException
from backend.database.repos.individuals import IndividualsRepo
from backend.database.repos.places import PlacesRepo


errors = {
    404: {'error': '404', 'message': 'Not found'},
    405: {'error': '405', 'message': 'Method not allowed'},
    500: {'error': '500', 'message': 'Internal server error'}
}

app = Flask(__name__)
individuals_repo = IndividualsRepo()
places_repo = PlacesRepo()


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
app.register_error_handler(Exception, handle_nothttp_exception)


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
        'year_of_excavation': sql_individual.year_of_excavation
    }


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    response = individuals_repo.get_all()
    individuals = [converter(ind) for ind in response]
    return jsonify(individuals), 200


@app.route("/api/v1/places/", methods=['GET'])
def get_all_places():
    return places_repo.get_all()


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    individual = converter(individuals_repo.get_by_id(individual_id))
    return jsonify(individual), 200


@app.route("/api/v1/places/<int:place_id>", methods=['GET'])
def get_place(place_id):
    return places_repo.get_by_id(place_id)


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    return individuals_repo.add(request.json), 201


@app.route("/api/v1/places/", methods=['POST'])
def create_place():
    new_place = {
        'title': request.json['title'],
        'category': request.json['category']
    }
    return places_repo.add(new_place)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def update_individual(individual_id):
    return individuals_repo.update(individual_id, request.json), 200


@app.route("/api/v1/places/<int:place_id>", methods=['PUT'])
def update_place(place_id):
    updates = {
        'title': request.json['title'],
        'category': request.json['category']
    }
    return places_repo.update(place_id, updates)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    return individuals_repo.delete(individual_id), 200


@app.route("/api/v1/places/<int:place_id>", methods=['DELETE'])
def del_place(place_id):
    return places_repo.delete(place_id)
