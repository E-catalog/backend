from flask import Flask, request, jsonify


app = Flask(__name__)

individuals = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
}
id = max(individuals)


@app.route("/api/v1/individuals/", methods=['GET'])
def get_all_individuals():
    list_individuals = list(individuals.values())
    return jsonify(list_individuals)


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    return individuals[individual_id]


@app.route("/api/v1/individuals/", methods=['POST'])
def create_individual():
    global id
    new_id = id + 1
    individuals[new_id] = {
        "id": new_id,
        "title": request.json['title'],
        "place": request.json['place']
        }
    id += 1
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

