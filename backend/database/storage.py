from backend.database.db import db_session
from backend.database.individuals_model import Individuals
from flask import jsonify


class SqlIndividualsRepo:

    def get_all(self):
        answer = db_session.query(Individuals).all()
        result = [str(ind) for ind in answer]

        return jsonify(result)

    def get_by_id(self, id):
        answer = db_session.query(Individuals).filter(Individuals.id == id)
        return jsonify(answer)

    def add():
        pass

    def update():
        pass

    def delete():
        pass
