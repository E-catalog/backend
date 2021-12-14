from flask import Flask, request


app = Flask(__name__)

individuals = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
}


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def update_individual(individual_id):
    individual = individuals[individual_id]
    individual['title'] = request.json.get('title', individual['title'])
    individual['place'] = request.json.get('place', individual['place'])
    return individual, 202
