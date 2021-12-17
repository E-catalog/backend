from flask import Flask, request, jsonify
from werkzeug.exceptions import InternalServerError, MethodNotAllowed, NotFound, HTTPException


errors = {
    404: {'error': '404', 'message': 'Not found'},
    405: {'error': '405', 'message': 'Method not allowed'},
    500: {'error': '500', 'message': 'Internal server error'}
}

individuals = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
}

app = Flask(__name__)

"""
@app.errorhandler(NotFound)
def handle_404(e):
    return errors[404], 404


@app.errorhandler(MethodNotAllowed)
def handle_405(e):
    return errors[405], 405


@app.errorhandler(InternalServerError)
def handle_500(e):
    return errors[500], 500


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    return errors[500], 500
"""

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
    list_individuals = list(individuals.values())
    return jsonify(list_individuals)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    return individuals[individual_id]


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    new_id = max(individuals) + 1
    individuals[new_id] = {
        "id": new_id,
        "title": request.json['title'],
        "place": request.json['place']
        }
    return individuals[new_id], 201


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def update_individual(individual_id):
    individual = individuals[individual_id]
    individual['title'] = request.json.get('title', individual['title'])
    individual['place'] = request.json.get('place', individual['place'])
    return individual


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    del individuals[individual_id]
    return {}, 204
