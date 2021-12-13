from flask import Flask, jsonify


app = Flask(__name__)

individuals = [
    {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев Курган"},
    {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев Курган"},
    {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев Курган"}
]


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    individual = filter(lambda x: x['id'] == individual_id, individuals)
    return next(individual)

