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
    1: {"id": 1, "title":"Мамаев Курган", "category": "Курган"},
    2: {"id": 2, "title":"Красный Курган", "category": "Курган"},
    3: {"id": 3, "title":"Синий Курган", "category": "Курган"}
    }



app = Flask(__name__)
#individuals_repo = IndividualsRepo()
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


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    return individuals_repo.get_all()


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    return individuals_repo.get_by_id(individual_id)


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    """
    new_individual = {
        'title': request.json['title'],
        'place': request.json['place']
    }
    """
    return individuals_repo.add(request.json)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def update_individual(individual_id):
    """
    updates = {
        'title': request.json['title'],
        'place': request.json['place']
    }
    """
    return individuals_repo.update(individual_id, request.json)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    return individuals_repo.delete(individual_id)


@app.route("/api/v1/places/", methods=['GET'])
def get_all_places():
    list_places = list(places.values())
    return jsonify(list_places)


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
    place = places[places_id]
    place['title'] = request.json.get('title',  place['title'])
    place['category'] = request.json.get('category', place['category'])
    return place

