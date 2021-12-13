from flask import Flask, request


app = Flask(__name__)

individuals = [
    {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
]


@app.route("/api/v1/individuals/<int:individual_id>", methods=['GET'])
def get_individual(individual_id):
    individual = filter(lambda x: x['id'] == individual_id, individuals)
    return next(individual)

@app.route("/api/v1/individuals", methods=['POST'])
def create_individual():
    id = individuals[-1]["id"] + 1
    new_individual = {
        "id": id,
        "title": request.json['title'],
        "place": request.json['place']
    }
    individuals.append(new_individual)
    return individuals[-1]
