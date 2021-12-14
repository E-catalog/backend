from flask import Flask, jsonify


app = Flask(__name__)

individuals = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев Курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев Курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев Курган"}
}


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    list_individuals = list(individuals.values())
    return jsonify(list_individuals)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    return individuals[individual_id]
