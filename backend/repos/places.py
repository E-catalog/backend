from backend.database.models import Places
from backend.database.session import db_session
from backend.schemas import Place


class PlacesRepo:

    def get_all(self) -> list[Places]:
        return db_session.query(Places).all()

    def get_by_id(self, uid: int):
        return db_session.query(Places).get(uid)

    def add(self, place: Place) -> Places:
        new_place = Places(
            name=place.name,
            head_of_excavations=place.head_of_excavations,
            type_of_burial_site=place.type_of_burial_site,
            coordinates=place.coordinates,
            comments=place.comments,
        )
        db_session.add(new_place)
        db_session.commit()
        return new_place

    def update(self, uid: int, update: Place) -> Places:
        place = db_session.query(Places).get(uid)

        place.name = update.name
        place.uid = update.uid
        place.head_of_excavations = update.head_of_excavations
        place.type_of_burial_site = update.type_of_burial_site
        place.coordinates = update.coordinates
        place.comments = update.comments

        db_session.commit()
        return place

    def delete(self, uid: int) -> None:
        individual = db_session.query(Places).get(uid)
        db_session.delete(individual)
        db_session.commit()
