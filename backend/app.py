from flask import Flask, jsonify


app = Flask(__name__)

individuals = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
}


@app.route("/api/v1/individuals/<int:individual_id>", methods=['DELETE'])
def del_individual(individual_id):
    del individuals[individual_id]
    return {}, 204
