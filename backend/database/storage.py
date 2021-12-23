from backend.database.db import db_session
from backend.database.individuals_model import Individuals


class SqlIndividualsRepo():

    def get_all():
        answer = db_session.query(Individuals).all()
        for ind in answer:
            return ind

    def get_by_id(id):
        return db_session.query(Individuals.id == id)

    def add():


    def update():


    def delete():

