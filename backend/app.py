from flask import Flask, request, jsonify
from werkzeug.exceptions import InternalServerError, MethodNotAllowed, NotFound, HTTPException
from backend.pl_storage import PlacesRepo
from backend.storage import IndividualsRepo
from backend.ztorage import PlacesRepo


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


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    return individuals_repo.get_all()


@app.route("/api/v1/places/", methods=['GET'])
def get_all_places():
    return places_repo.get_all()


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    return individuals_repo.get_by_id(individual_id)


@app.route("/api/v1/places/<int:places_id>", methods=['GET'])
def get_places(places_id):
    return places_repo.get_by_id(places_id)


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    new_individual = {
        'title': request.json['title'],
        'place': request.json['place']
    }
    return individuals_repo.add(new_individual)


@app.route("/api/v1/places/", methods=['POST'])
def change_places():
    new_places = {
        'title': request.json['title'],
        'category': request.json['category']
    }
    return places_repo.add(new_places)


@app.route("/api/v1/places/<int:places_id>", methods=['PUT'])
def update_places(places_id):
    updates = {
        'title': request.json['title'],
        'category': request.json['category']
    }
    return places_repo.update(places_id, updates)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    return individuals_repo.delete(individual_id)



@app.route("/api/v1/places/", methods=['GET'])
def get_all_places():
    return places_repo.get_all()


@app.route("/api/v1/places/<int:places_id>", methods=['GET'])
def get_place(places_id):
    return places_repo.get_by_id(places_id)


@app.route("/api/v1/places/", methods=['POST'])
def create_place():
    new_place = {
        'title': request.json['title'],
        'category': request.json['category']
    }
    return places_repo.add(new_place)


@app.route("/api/v1/places/<int:place_id>", methods=['PUT'])
def update_place(place_id):
    updates = {
        'title': request.json['title'],
        'category': request.json['category']
    }
    return places_repo.update(place_id, updates)


@app.route("/api/v1/places/<int:place_id>", methods=['DELETE'])
def del_place(place_id):
    return places_repo.delete(place_id)

