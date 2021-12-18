from flask import Flask, request, jsonify
from werkzeug.exceptions import InternalServerError, MethodNotAllowed, NotFound, HTTPException
from backend.storage.storage import IndividualsRepo


errors = {
    404: {'error': '404', 'message': 'Not found'},
    405: {'error': '405', 'message': 'Method not allowed'},
    500: {'error': '500', 'message': 'Internal server error'}
}

app = Flask(__name__)
individuals_repo = IndividualsRepo()


def handle_404(e):
    return errors[404], 404


def handle_405(e):
    return errors[405], 405


def handle_500(e):
    return errors[500], 500


#def handle_nothttp_exception(e):
#    if not isinstance(e, HTTPException):
#        return errors[500], 500


app.register_error_handler(NotFound, handle_404)
app.register_error_handler(MethodNotAllowed, handle_405)
app.register_error_handler(InternalServerError, handle_500)
#app.register_error_handler(Exception, handle_nothttp_exception)


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    individuals_repo.get_all()


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    individuals_repo.get_by_id(individual_id)


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    new_individual = {
        'title': request.json['title'],
        'place': request.json['place']
    }
    individuals_repo.add(new_individual)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def update_individual(individual_id):
    updates = {
        'title': request.json['title'],
        'place': request.json['place']
    }
    individuals_repo.update(individual_id, updates)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    individuals_repo.delete(individual_id)


places = {
    "id": 5,
    "title": "Мамаев Курган",
    "category": "Курган",
}

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

