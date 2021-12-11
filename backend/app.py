from flask import Flask


app = Flask(__name__)

items = {
    '11': {"title": "Неопознанный объект #11", "place": "Мамаев Курган"},
    '12': {"title": "Неопознанный объект #12", "place": "Мамаев Курган"},
    '13': {"title": "Неопознанный объект #13", "place": "Мамаев Курган"}
}


@app.route("/api/v1/individuals/<individual_id>", methods=['GET'])
def data(individual_id):
    return items[individual_id]
