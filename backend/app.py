from flask import Flask, request

app = Flask(__name__)

individuals = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
}
id = max(individuals)


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
