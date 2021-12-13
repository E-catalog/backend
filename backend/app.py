from flask import Flask, request


app = Flask(__name__)

individuals = [
    {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
]


@app.route("/api/v1/individuals/<int:individual_id>", methods=['PUT'])
def data(individual_id):
    individual = next(filter(lambda x: x['id'] == individual_id, individuals))
    individual['title'] = request.json.get('title', individual['title'])
    individual['place'] = request.json.get('place', individual['place'])
    return individual, 201
