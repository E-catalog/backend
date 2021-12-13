from flask import Flask, jsonify


app = Flask(__name__)

individuals = [
    {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
]


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def data(individual_id):
    global individuals
    individual = next(filter(lambda x: x['id'] == individual_id, individuals))
    individuals.remove(individual)
    return jsonify(individuals)
